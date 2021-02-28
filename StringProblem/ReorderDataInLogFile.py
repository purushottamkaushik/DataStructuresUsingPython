class Solution:
    def reorderLogFiles(self, logs):

        letter_logs, digit_logs = [], []

        for i in range(len(logs)):
            second_word = logs[i].split()[1]
            if second_word.isdigit():
                digit_logs.append(logs[i])
            else:
                letter_logs.append(logs[i])

        letter_logs.sort(key=lambda x: x.split()[0])
        letter_logs.sort(key=lambda x: x.split()[1:])

        return letter_logs + digit_logs
