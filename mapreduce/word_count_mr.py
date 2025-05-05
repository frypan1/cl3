from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"[\w']+")

class MRWordCount(MRJob):
    def mapper(self, _, line):
        for word in WORD_REGEXP.findall(line):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()

## sent count

# from mrjob.job import MRJob
# import re

# regex = re.compile(r'[^.!?]*[.!?]')

# class MRSentCount(MRJob):
#     def mapper(self,_,lines):
#         for _ in regex.findall(lines):
#             yield "Sentence(s)", 1
#     def reducer(self, sent, counts):
#         yield sent, sum(counts)

# if __name__ == "__main__":
#     MRSentCount.run()