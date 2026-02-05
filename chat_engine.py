from vehicle_data import vehicles

class ChatBot:
    def __init__(self):
        # Conversation States
        self.STATES = [
            "WELCOMING",
            "ASK_NAME",
            "ASK_VEHICLE_TYPE",
            "ASK_FUEL",
            "ASK_BUDGET",
            "ASK_USAGE",
            "RECOMMENDING",
            "FINISHED"
        ]
        self.current_state_index = 0
        self.user_preferences = {}
        self.user_name = ""

    def _get_state(self):
        return self.STATES[self.current_state_index]

    def _next_state(self):
        if self.current_state_index < len(self.STATES) - 1:
            self.current_state_index += 1

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        state = self._get_state()

        if user_input in ["reset", "restart", "start over", "0"]:
            self.__init__()
            return "Okay, let's start over! Hello! I'm your Vehicle Recommendation Assistant. What's your name?"

        if state == "WELCOMING":
            self._next_state() # Move to ASK_NAME
            return "Hello! I'm your Vehicle Recommendation Assistant. I can help you find the perfect ride.\n\nFirst, what should I call you?"

        if state == "ASK_NAME":
            if user_input:
                self.user_name = user_input.title()
                self._next_state() # Move to ASK_VEHICLE_TYPE
                return (f"Nice to meet you, {self.user_name}! What type of vehicle are you looking for?\n"
                        "1. Car\n"
                        "2. Bike\n"
                        "3. SUV\n"
                        "4. EV\n"
                        "\n(Type 1, 2, 3, or 4)")
            else:
                return "I didn't quite catch that. What is your name?"

        if state == "ASK_VEHICLE_TYPE":
            # Map numbers/text to types
            choice = None
            if user_input == "1" or "car" in user_input: choice = "car"
            elif user_input == "2" or "bike" in user_input or "scooter" in user_input: choice = "bike"
            elif user_input == "3" or "suv" in user_input: choice = "suv"
            elif user_input == "4" or "ev" in user_input: choice = "ev"

            if choice:
                self.user_preferences["type"] = choice
                self._next_state() # Move to ASK_FUEL
                
                # If EV, skip fuel question
                if choice == "ev":
                    self.user_preferences["fuel"] = "electric"
                    self._next_state() # Skip ASK_FUEL
                    return (f"Great selection! Since it's an EV, we'll skip the fuel type.\n\n"
                            "What is your budget range?\n"
                            "1. Low (< 10 Lakh / < 1.5 Lakh)\n"
                            "2. Medium (10-25 Lakh / 1.5-4 Lakh)\n"
                            "3. High (> 25 Lakh / > 4 Lakh)\n"
                            "\n(Type 1, 2, or 3)")

                return (f"Got it, a {choice}. What fuel type do you prefer?\n"
                        "1. Petrol\n"
                        "2. Diesel\n"
                        "3. Electric\n"
                        "4. Any\n"
                        "\n(Type 1, 2, 3, or 4)")
            else:
                return "Please select a valid option (1-4) or type the name."

        if state == "ASK_FUEL":
            choice = None
            if user_input == "1" or "petrol" in user_input: choice = "petrol"
            elif user_input == "2" or "diesel" in user_input: choice = "diesel"
            elif user_input == "3" or "electric" in user_input: choice = "electric"
            elif user_input == "4" or "any" in user_input: choice = "any"

            if choice:
                self.user_preferences["fuel"] = choice
                self._next_state() # Move to ASK_BUDGET
                return ("Understood. Now, what is your budget range?\n"
                        "1. Low (< 10L)\n"
                        "2. Medium (10-25L)\n"
                        "3. High (> 25L)\n"
                        "\n(Type 1, 2, or 3)")
            else:
                return "Please select a valid option (1-4)."

        if state == "ASK_BUDGET":
            choice = None
            if user_input == "1" or "low" in user_input: choice = "low"
            elif user_input == "2" or "medium" in user_input: choice = "medium"
            elif user_input == "3" or "high" in user_input: choice = "high"
            
            if choice:
                self.user_preferences["budget"] = choice
                self._next_state() # Move to ASK_USAGE
                return ("Okay. Finally, what will be your primary usage?\n"
                        "1. City (Daily Commute)\n"
                        "2. Highway (Long Trips)\n"
                        "3. Family (Comfort)\n"
                        "\n(Type 1, 2, or 3)")
            else:
                return "Please select a valid budget option (1, 2, or 3)."

        if state == "ASK_USAGE":
            choice = None
            if user_input == "1" or "city" in user_input: choice = "city"
            elif user_input == "2" or "highway" in user_input: choice = "highway"
            elif user_input == "3" or "family" in user_input: choice = "family"

            if choice:
                self.user_preferences["usage"] = choice
                self._next_state() # Move to RECOMMENDING
                return self.generate_recommendation()
            else:
                return "Please select a valid usage option (1, 2, or 3)."

        if state == "RECOMMENDING" or state == "FINISHED":
            return "I've already given my recommendations. Type 'reset' to start over!"

        return "I'm not sure I understood. Could you try again?"

    def generate_recommendation(self):
        """
        Filters the vehicle list and returns a formatted string with results.
        Enforces strict Type filtering.
        """
        prefs = self.user_preferences
        matches = []
        
        # STRICT FILTER: Only consider vehicles of the requested type
        # Treat 'suv' and 'car' somewhat flexibly if needed, but for now keep strict.
        # User explicitly chooses Car, Bike, SUV, EV.
        
        relevant_vehicles = [v for v in vehicles if v["type"] == prefs.get("type")]

        # If strict filtering returns nothing (unlikely with our data), we might relax or show generic message.
        if not relevant_vehicles:
             return f"I see you're looking for a {prefs.get('type')}, but I couldn't find any in my current database. Try a different category!"

        # Scoring system for the remaining attributes
        for v in relevant_vehicles:
            score = 0
            # Removed Type scoring since we are valid-filtering now.
            
            # Fuel match
            if prefs.get("fuel") != "any" and v["fuel"] == prefs.get("fuel"): score += 1
            
            # Budget match
            if v["budget_range"] == prefs.get("budget"): score += 1
            
            # Usage match
            if v["usage"] == prefs.get("usage"): score += 1
            
            matches.append((score, v))

        # Sort by score descending
        matches.sort(key=lambda x: x[0], reverse=True)
        
        # Get top 3
        # Use a looser cutoff since we already filtered by type
        top_picks = [m[1] for m in matches[:3]]

        if not top_picks:
            self._next_state()
            return f"Hmm, I couldn't find a perfect match for a {prefs['type']} with those specific criteria. Try typing 'reset' and broadening your options!"

        response = f"Based on your needs ({prefs['type']}, {prefs.get('fuel', '')}, {prefs['budget']} budget), here are my top recommendations for you, {self.user_name}:\n"
        
        for i, car in enumerate(top_picks, 1):
            response += f"\n{i}. **{car['name']}** - {car['price']}\n"
            response += f"   - *Mileage*: {car['mileage']}\n"
            response += f"   - *Why*: {car['features']}\n"
            response += f"   - {car['description']}\n"

        self._next_state() # Move to FINISHED
        response += "\nHope this helps! Type 'reset' if you want to search again."
        return response
