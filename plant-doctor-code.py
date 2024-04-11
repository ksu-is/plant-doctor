

recommendations = {
    "Leaves turning yellow near the tip": "Leaves turning yellow at the tips indicates that the plant is not receiving enough water. Try watering thoroughly until water comes out of the drainage holes.",
    "Leaves turning yellow near the stem": "Leaves turning yellow at the base indicates that the plant is receiving too much water. The 'poke' test is an easy way to determine if your plant needs water. Try inserting a wooden stick or your finger into the top inch of soil. Once the top inch of soil feels dry, give the plant water!",
    "Plant not growing very quickly": "When a plant is not growing much, it may indicate that the plant is not in optimal conditions. Make sure that the plant is receiving lots of warmth, sunlight, and an appropriate amount of water.",
}

def plant_doctor():
    print("Welcome to The Plant Doctor!")
    issue = input("What is going on with your plant? ")

    #iterate through issue to see if there are keywords in common with the recommendations
    for symptom, recommendation in recommendations.items():
        if any(keyword.lower() in issue.lower() for keyword in symptom.lower().split()):
            print({recommendation})
            return

    print("No specific recommendation found for this issue.")

plant_doctor()