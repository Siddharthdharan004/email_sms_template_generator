import os

# Create a folder to save templates
if not os.path.exists("templates"):
    os.makedirs("templates")

def generate_template(scenario, tone):
    """Generate an email or SMS template based on the scenario and tone."""
    if tone.lower() == "formal":
        template = f"""
        Subject: {scenario.title()}

        Dear [Recipient's Name],

        I hope this message finds you well. I am writing to inform you about {scenario.lower()}.
        
        [Provide details about the scenario here.]
        
        Thank you for your attention to this matter. Please feel free to reach out if you have any questions or require further clarification.

        Best regards,
        [Your Name]
        """
    elif tone.lower() == "informal":
        template = f"""
        Hey [Recipient's Name],

        Hope you're doing great! Just wanted to let you know about {scenario.lower()}.
        
        [Add details here in a conversational tone.]
        
        Let me know if you need anything or want to chat more about it!

        Cheers,
        [Your Name]
        """
    else:
        return "Invalid tone. Please select either 'formal' or 'informal'."
    
    return template.strip()

def save_template(template, filename):
    """Save the generated template to a file."""
    filepath = os.path.join("templates", filename)
    with open(filepath, "w") as file:
        file.write(template)
    print(f"Template saved to {filepath}")

def main():
    print("Welcome to the Email/SMS Template Generator!")
    scenario = input("Enter the scenario (e.g., meeting invitation, thank-you note): ").strip()
    tone = input("Enter the tone (formal/informal): ").strip()
    
    template = generate_template(scenario, tone)
    if "Invalid tone" in template:
        print(template)
        return
    
    print("\nGenerated Template:")
    print(template)
    
    save_option = input("\nDo you want to save this template? (yes/no): ").strip().lower()
    if save_option == "yes":
        filename = input("Enter a filename (without extension): ").strip() + ".txt"
        save_template(template, filename)
    else:
        print("Template not saved.")

if __name__ == "__main__":
    main()
