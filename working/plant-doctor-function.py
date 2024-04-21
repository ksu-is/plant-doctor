print("Welcome to Plant Care Assistant!")
print("Please describe any issues you're facing with your plant using a sentence:")

# Define a dictionary of plant care recommendations based on keywords
care_recommendations = {
    'yellow': [
        "Yellow leaves at the base may indicate overwatering. Try reducing the frequency of watering and ensure proper drainage.",
        "Yellow leaves at the tip may indicate nutrient deficiency. Consider fertilizing the plant with a balanced fertilizer."
    ],
    'brown': [
        "Brown spots may indicate a fungal infection. Consider trimming affected areas and applying a fungicide."
    ],
    'wilting': [
        "Wilting can be a sign of underwatering. Make sure the plant is receiving adequate water, and adjust watering frequency as needed."
    ],
    'leggy': [
        "Leggy growth often occurs in low light conditions. Move the plant to a brighter location and consider pruning to encourage bushier growth."
    ]
    # Add more care recommendations as needed
}

# Function to provide recommendations based on user input sentence
def provide_recommendations(user_input):
    keywords = []
    for word in user_input.split():
        for keyword in care_recommendations.keys():
            if keyword.lower() in word.lower():
                keywords.append(keyword)
    recommendations = []
    for keyword in keywords:
        recommendations.extend(care_recommendations.get(keyword, []))
    return recommendations

# Main function to interact with the user
def main():
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'quit':
            print("Thank you for using Plant Care Assistant. Goodbye!")
            break
        else:
            recommendations = provide_recommendations(user_input)
            if recommendations:
                print("\nRecommendations:")
                for recommendation in recommendations:
                    print("- " + recommendation)
            else:
                print("No matching recommendations found. Please try different keywords or describe the issue in more detail.")

if __name__ == "__main__":
    main()
