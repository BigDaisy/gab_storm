import logging

from pyleus.storm import SimpleBolt

log = logging.getLogger('splitter')


class SplitWordsBolt(SimpleBolt):

    OUTPUT_FIELDS = ["word"]

    def process_tuple(self, tup):
        line, = tup.values
        log.info(line)


if __name__ == '__main__':
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     filename='/tmp/word_count_split_words.log',
    #     format="%(message)s",
    #     filemode='a',
    # )
    SplitWordsBolt().run()
