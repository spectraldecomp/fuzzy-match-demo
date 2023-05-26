from rapidfuzz import process, fuzz


# Loads company data with user-specified keywords for each company
def load_companies(file_path):
    companies = {}

    with open(file_path, 'r') as file:
        num_companies = int(file.readline().strip())

        for _ in range(num_companies):
            line = file.readline().strip()
            company_name, company_keywords = line.split(':')
            company_name = company_name.strip()
            company_keywords = [keyword.strip() for keyword in company_keywords.strip('[]').split(',')]

            companies[company_name] = company_keywords

    return companies

# Loads data to be processed
def load_data(file_path):
    data = []

    with open(file_path, 'r') as file:
        num_data = int(file.readline().strip())

        for _ in range(num_data):
            line = file.readline().strip()
            data.append(line)

    return data

 # Finds relevance of each data point to specified keyword and its associated company
def process_keyword(keyword, data):

    print(f'Processing keyword: {keyword}')
    x = process.extract(keyword, data, limit=len(data))
    return x

def main():
    companies = load_companies('data/companies.txt')
    data = load_data('data/data.txt')
    sorted_data = []
    for company in companies:
        sorted_company_data = []
        for keyword in companies[company]:
            sorted_keyword = process_keyword(keyword, data)
            # Add each element of sorted_keyword to sorted_company_data if it is not already in sorted_company_data.
            # We check if it is already in sorted_company_data by checking if the third element of the tuple is present in
            # any of the elements of sorted_company_data. If it is not, then we add that element. #We also overwrite the element
            # if it is already present in sorted_company_data but with a lower score.
            for element in sorted_keyword:
                if not any(element[2] in sublist for sublist in sorted_company_data):
                    sorted_company_data.append(element)
                else:
                    for i in range(len(sorted_company_data)):
                        if sorted_company_data[i][2] == element[2] and sorted_company_data[i][1] < element[1]:
                            sorted_company_data[i] = element
        sorted_company_data.sort(key=lambda x: x[1], reverse=True)
        sorted_data.append(sorted_company_data)

    print((sorted_data[1]))




if __name__ == '__main__':
    main()

