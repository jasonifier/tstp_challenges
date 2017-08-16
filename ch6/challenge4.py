#!/usr/bin/env python3

q_string = "Where now? Who now? When now?"
q_list = q_string.split("?")
q_list.pop()
questions = [q.strip() + "?" for q in q_list]
print(questions)
