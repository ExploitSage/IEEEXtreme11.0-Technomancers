import sys
import random
topics = {}
books = []
for line in sys.stdin:
        vals = line.strip().split(" ")
        time = int(vals[0])
        n_topics = len(vals)
        books.append([time] + vals[1:])

for iterate in range(50):
        topics = {}
        random.shuffle(books)

        for b_index,book in enumerate(books):
                vals = book[1:]
                time = book[0]
                for i in range(len(vals)):
                        if vals[i] not in topics or books[topics[vals[i]]][0] > time:
                                topics[vals[i]] = b_index

                 
  
         




        book_list = set([topics[x] for x in topics])
        if(iterate == 0):
                min_time = sum([books[x][0] for x in book_list])
        for i in range(10):
                for b_index,book in enumerate(books):
                        c_time = min_time + book[0]
                        topic_copy = dict(topics)
                        for topic in book[1:]:
                                topic_copy[topic] = b_index

                        book_list = set([topic_copy[x] for x in topic_copy])
                        new_min_time = sum([books[x][0] for x in book_list])
                        if new_min_time < min_time:
                                min_time = new_min_time
                                topics = topic_copy

print(min_time)
