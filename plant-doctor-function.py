import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def search_and_recommend(data, keywords):
    recommendations = []
    for item in data:
        for keyword in keywords:
            if keyword.lower() in item['Keywords'].lower():
                recommendations.append(item['Recommendation'])
                break  # Once a match is found, no need to check further
    return recommendations

def plant_doctor():
    csv_file_path = "symptom_keywords.csv"
    data = read_csv_file(csv_file_path)

    user_input = input("Enter keywords (comma-separated): ").strip().split(',')
    recommendations = search_and_recommend(data, user_input)

    if recommendations:
        print("Recommendations:")
        for recommendation in recommendations:
            print("-", recommendation)
    else:
        print("No recommendations found.")

plant_doctor()
