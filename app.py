from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        
        full_name = "HarshGoyal"
        dob = "24032004"
        user_id = f"{full_name.lower()}_{dob}"
        email = "harsh.goyal2022@vitstudent.ac.in"
        roll_number = "22BCE2789"

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        
        for item in data:
            if isinstance(item, str) and item.isalpha():
                alphabets.append(item.upper())
            elif isinstance(item, str) and item.isnumeric():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
                total_sum += num
            elif isinstance(item, str):
                # Check for special characters using regex
                if re.match(r'[^a-zA-Z0-9]', item):
                    special_characters.append(item)

        # Logic for concat_string
        all_alpha_chars = []
        for item in data:
            if isinstance(item, str):
                for char in item:
                    if char.isalpha():
                        all_alpha_chars.append(char)
        
        all_alpha_chars.reverse()
        
        concat_string = ""
        for i, char in enumerate(all_alpha_chars):
            if i % 2 == 1:
                concat_string += char.lower()
            else:
                concat_string += char.upper()

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "even_numbers": even_numbers,
            "odd_numbers": odd_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)