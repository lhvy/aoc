import util

lines = util.get_input_lines()

part_a = 0

for l in lines:
    for r in l.split(","):
        if r == "":
            continue
        start, end = [int(x) for x in r.split("-")]
        for i in range(start, end + 1):
            n_str = str(i)
            len_str = len(n_str)
            if len_str % 2 != 0:
                continue
            if n_str[0 : (len_str // 2)] == n_str[(len_str // 2) :]:
                part_a += i

print("Part a: ", part_a)

part_b = 0

for l in lines:
    for r in l.split(","):
        if r == "":
            continue
        start, end = [int(x) for x in r.split("-")]
        for i in range(start, end + 1):
            n_str = str(i)
            len_str = len(n_str)
            chunks = len_str
            while chunks > 1:
                chunk_len = len_str // chunks
                if len_str % chunks != 0 or chunk_len == len_str:
                    chunks -= 1
                    continue
                base = n_str[0:chunk_len]
                n_invalid = True
                for j in range(1, chunks):
                    # print(
                    #     chunks,
                    #     chunk_len,
                    #     base,
                    #     n_str[j * chunk_len : j * chunk_len + chunk_len],
                    # )
                    if base != n_str[j * chunk_len : j * chunk_len + chunk_len]:
                        chunks -= 1
                        n_invalid = False
                        break
                if n_invalid:
                    # print(i, chunk_len, chunks)
                    part_b += i
                    break

print("Part b: ", part_b)
