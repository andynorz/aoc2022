def main(inputs: list):

    results = list()
    chunk_size = 4
    for input in inputs:
        for i in range(len(input)):
            # Scan 4 chars, make unique set
            chunk = set(input[i:i+4])

            # If size == chunksize, then there are no dupes
            if len(chunk) == chunk_size:
                results.append(chunk_size + i)
                break
    return results
