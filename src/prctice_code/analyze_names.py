def analyze_names(names):
    unique_dict = {
        "unique" : set(names),
        "count" : len(set(names)),
        "most" : sorted(list(set(names)))
    }

    for key , value in unique_dict.items():
        print(f'{key} : {value}')

    return unique_dict

if __name__ == "__main__":
    names = list(input().split())
    analyze_names(names)