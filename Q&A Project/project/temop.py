def count_triplets(arr, d):
    st = set()
    
    for i in range(len(arr)):
        hashset = set()
        for j in range(i + 1, len(arr)):
            # Calculate the 3rd element:
            third = d-(arr[i] + arr[j])

            # Find the element in the set:
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])

    # store the set in the answer:
    ans = list(st)
    
    # Count triplets with sum divisible by d:
    count = 0
    for triplet in ans:
        if sum(triplet) % d == 0:
            count += 1

    return count


arr = [2,3,1,6]
d = 3  # replace with your desired value of d
result = count_triplets(arr, d)

print(f"Number of distinct triplets with sum divisible by {d}: {result}")
