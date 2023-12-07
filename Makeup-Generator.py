"""
Final Project: Makeup Generator    
=======================
The Makeup Generator Project simplifies and customizes the process of choosing makeup by giving personalized suggestions for face foundation based on the user's skin type. 
It helps tackle the common challenge of finding makeup products that match individual skin characteristics.

NAME: Aziza Temirova
SEMESTER: Fall 2023
COURSE: CS5001
"""

def get_foundation_type(skin_type):
    """
    Get recommended foundation types based on the user's skin type.

    Parameters:
    - skin_type (str): User's skin type (e.g., "oily", "dry", "combination").

    Returns:
    - str: Recommended foundation types.
    """
    # Map different skin types to corresponding foundation types
    if skin_type == "oily":
        return "Oil-Free, Matte, Powder, Long Wearing, Water-Based, Mineral, Non-Comedogenic, Matte Mousse"
    elif skin_type == "dry":
        return "Hydrating, Dewy, Liquid, Cream, Stick, Serum, BB Creams and CC Creams, Mineral, Hyaluronic Acid, Oil-Based"
    elif skin_type == "combination":
        return "Matte-Luminous Foundations, Oil-Control Foundations, Water-Based Foundations"


def get_primer(skin_type):
    """
    Get recommended primer based on the user's skin type.

    Parameters:
    - skin_type (str): User's skin type (e.g., "oily", "dry", "combination").

    Returns:
    - str: Recommended primer type.
    """
    # Map different skin types to corresponding primer types
    if skin_type == "oily":
        return "Mattifying, Oil-free, Water-based, Pore-Filling, Long Wearing"
    elif skin_type == "dry":
        return "Hydrating, Luminizing, Nourishing, Cream-Based, Radiance-Boosting"
    elif skin_type == "combination":
        return "Balancing, Two-in-One, Oil-Control, Weightless, Blur + Hydrate"


def get_setting_spray(skin_type):
    """
    Get recommended setting spray based on the user's skin type.

    Parameters:
    - skin_type (str): User's skin type (e.g., "oily", "dry", "combination").

    Returns:
    - str: Recommended setting spray type.
    """
    # Map different skin types to corresponding setting spray types
    if skin_type == "oily":
        return "Matte Finish Setting Sprays, Oil-Free Setting Sprays, Long-Wearing Setting Sprays, Oil-Control Setting Sprays, Mattifying Setting Sprays"
    elif skin_type == "dry":
        return "Hydrating Setting Sprays, Dewy Finish Setting Sprays, Nourishing Setting Sprays, Refreshing Setting Sprays, Glow-Enhancing Setting Sprays"
    elif skin_type == "combination":
        return "Balancing Setting Sprays, Two-in-One Setting Sprays, Weightless Setting Sprays, Hydrating + Mattifying Setting Sprays, Dual-Action Setting Sprays"


def main():
    """
    Main function to interact with the user and provide makeup recommendations.
    """
    print("Welcome to Makeup Helper To Find You The Perfect Base!")
    
    # Take user input for skin type
    skin_type = input("Input your skin type: ")
    foundation_recommendation = get_foundation_type(skin_type)
    
    print(f"Recommend Type of Foundation for your skin type: {foundation_recommendation}")
    
    # Take user input for primer and setting spray preference
    want_primer_setting_spray = input("Would you like matching primer and setting spray? (Y/N): ")
    
    if want_primer_setting_spray.lower() == "y":
        primer_recommendation = get_primer(skin_type)
        setting_spray_recommendation = get_setting_spray(skin_type)
        
        print(f"Recommended Primer: {primer_recommendation}")
        print(f"Recommended Setting Spray: {setting_spray_recommendation}")
    elif want_primer_setting_spray.lower() == "n":
        print("Enjoy your match!")

if __name__ == "__main__":
    main()