from unicodedata import category
from collections import namedtuple
from os import listdir, getcwd
from os.path import join
import re


Token = namedtuple('Token', ('word', 'type', 'line', 'start', 'end', 'filename'))


class Tokenizer:

    def __init__(self):
        self._tokens_list = []
        self._tokens_by_file = {}
        self._index_dict = {}
        self._file_names = []
        self._work_dir = ''

    @staticmethod
    def get_type(char_type: str) -> str:
        type_dict = {
            'Lm': 'alpha',
            'Lt': 'alpha',
            'Lu': 'alpha',
            'Ll': 'alpha',
            'Lo': 'alpha',
            'Nd': 'digit',
            'Po': 'punctuation',
            'Pe': 'punctuation',
            'Pf': 'punctuation',
            'So': 'punctuation',
            'Zs': 'space',
            'Cc': 'space',
            'Sk': 'other',
            'Sm': 'other',
        }
        return type_dict[char_type]

    def tokenizer(self, string: str, line: int = 0, filename: str = '') -> list:
        def save_vars() -> dict:
            return {
                'word': ''.join(tmp),
                'type': kind,
                'line': line,
                'start': start,
                'end': start + len(tmp),
                'filename': filename,
            }
        tmp = []
        result = []
        kind = ''
        start = 0
        for n, char in enumerate(string):
            cat = self.get_type(category(char))
            if cat == kind:
                tmp.append(char)
            else:
                if kind in ('alpha', 'digit'):
                    result.append(Token(**save_vars()))
                start = n
                tmp.clear()
                tmp.append(char)
                kind = cat
        else:
            if kind in ('alpha', 'digit'):
                result.append(Token(**save_vars()))
        return result

    def add_from_file(self, name: str, dir_name: str):
        with open(join(dir_name, name)) as file:
            self._tokens_by_file[name] = []
            for n, string in enumerate(file):
                tokens = self.tokenizer(string, n, name)
                self._tokens_list.append(tokens)
                self._tokens_by_file[name].append(tokens)
        self.dict_by_tokens()

    def add_directory(self, dir_name: str = '') -> None:
        dir_name = join(getcwd(), dir_name)
        self._work_dir = dir_name
        self._file_names = sorted(listdir(dir_name))
        for name in self._file_names:
            if name.endswith('.txt'):
                self.add_from_file(name, dir_name)

    def dict_by_tokens(self) -> None:
        result = dict()
        for tokens in self._tokens_list:
            for token in tokens:
                result[token.word] = result.get(token.word, dict())
                result[token.word][token.filename] = result[token.word].get(token.filename, [])
                result[token.word][token.filename].append([token.line, token.start, token.end])
        self._index_dict = result

    def simple_search(self, query: str) -> None:
        try:
            query, limit, offset = query.split(',')
            limit = self._validate_input(limit)
            offset = self._validate_input(offset)
        except ValueError:
            print(f'{query} is Incorrect input')
            return
        query_tokens = self.tokenizer(query)
        res = {}
        for doc in self._file_names[offset:][:limit]:
            inner_res = []
            for token in query_tokens:
                try:
                    inner_res.extend(self._index_dict[token.word][doc])
                except KeyError:
                    break
            else:
                res[doc] = sorted(inner_res)
        print('; '.join(f'{k}: {v}' for k, v in res.items()))

    def context_window(self, query: str):
        try:
            file, position, window = query.split(';')
            position = list(map(self._validate_input, position.split(',')))
            window = self._validate_input(window)
        except ValueError:
            print(f'{query} is Incorrect input')
            return
        with open(join(self._work_dir, file)) as f:
            line = f.readlines()[position[0]].rstrip()
        token_pos = [n for n, tok in enumerate(self._tokens_by_file[file][position[0]])
                     if [tok.start, tok.end] == position[1:]][0]
        tokens_window = self._tokens_by_file[file][position[0]][
                        self._validate_input(token_pos - window):token_pos + window + 1]
        print(f'{line}|{[position]}|{tokens_window[0].start}|{tokens_window[-1].end}' if window else '')

    def upg_context(self, query_0: str, query_1: str):
        def read_query(qr: str) -> tuple:
            tx, pos, w_st, w_end = qr.split('|')
            pos = list(map(self._validate_input, pos[2:-2].split(', ')))
            return tx, pos, int(w_st), int(w_end)

        def make_bold(string: str) -> str:
            return f'<b>{string}</b>'

        def splitter(string: str, dots: list) -> list:
            return [string[dots[i]:dots[i + 1]] for i in range(len(dots) - 1)]

        def merge(words_pos: list, brd: list, txt: str, over_lap: bool) -> str:
            result = []
            if over_lap:
                poses_list = [brd[0][0]] + words_pos[0][1:] + words_pos[1][1:] + [brd[1][1]]
                result = splitter(txt, poses_list)
                result[1] = make_bold(result[1])
                result[3] = make_bold(result[3])
                return '|'.join([''.join(result)] + list(map(str, (words_pos, brd[0][0], brd[1][1]))))
            for b, w_p in zip(brd, words_pos):
                poses_list = b[:1] + w_p[1:] + b[1:]
                result_in = splitter(txt, poses_list)
                result_in[1] = make_bold(result_in[1])
                result.append('|'.join([''.join(result_in)] + list(map(str, ([w_p], b[0], b[1])))))
            return '\n'.join(result)

        re_pattern = re.compile(r'\b[^.!?]+[.!?]+')
        text_0, position_0, start_0, end_0 = read_query(query_0)
        text_1, position_1, start_1, end_1 = read_query(query_1)
        sentences = {sent: [text_0.index(sent), text_0.index(sent) + len(sent)] for sent in re_pattern.findall(text_0)}
        overlap = end_0 > start_1
        positions = [position_0, position_1]
        borders = []
        for position in positions:
            for sent, brs in sentences.items():
                if brs[0] <= position[1] <= brs[1]:
                    borders.append(brs)
        print(merge(positions, borders, text_0, overlap))

    @staticmethod
    def _validate_input(lim) -> int:
        return 0 if int(lim) < 0 else int(lim)

    def __repr__(self):
        print(self._tokens_by_file)
        return '\n'.join(
            f'{t[0]} | {t[2]}_{t[3]}_{t[4]} | {t[5]}' for token in self._tokens_list for t in token
        )


def main():
    tokens = Tokenizer()
    tokens.upg_context(input(), input())


if __name__ == '__main__':
    main()