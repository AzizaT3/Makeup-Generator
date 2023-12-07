# Final Project Report

* Student Name: Aziza Temirova
* Github Username: AzizaT3 
* Semester: Fall 2023
* Course: CS5001



## Description 
General overview of the project, what you did, why you did it, etc. 

The Makeup Generator Project aims to streamline and personalize the makeup selection process by providing tailored recommendations for face foundation based on the user's skin type. The project addresses the common challenge of choosing the right makeup products that complement individual skin characteristics.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

- The program greets users with a welcoming interface, ensuring ease of use when inputting their skin type for personalized recommendations.
- Receive dynamic suggestions for suitable foundation types based on your skin type, addressing specific needs like oil control, hydration, and coverage preferences.
-  Users can opt for matching primer and setting spray recommendations, enhancing the overall makeup routine. The program considers the user's skin type to provide products that complement their desired finish.

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

The program will welcome you and prompt you to input your skin type.
Enter your skin type as "oily," "dry," or "combination" and press Enter.
Based on your input, the program will recommend types of foundation suitable for your skin type.
The program will then ask if you would like recommendations for matching primer and setting spray.
Type "Y" for yes or "N" for no and press Enter.
If you chose "Y" for primer and setting spray recommendations, the program will provide suggestions for these products.


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

1. git clone [repository_url]
2. cd [project_directory]
3. pip install -r requirements.txt
4. Run the Project: Execute the main script to start the program:


## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

The complexity of mapping different skin types to specific makeup products required careful consideration. It involved creating comprehensive conditional statements to cover various scenarios.



## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)


Welcome to Makeup Helper To Find You The Perfect Base!
Input your skin type: oily
Recommend Type of Foundation for your skin type: Oil-Free, Matte, Powder, Long Wearing, Water-Based, Mineral, Non-Comedogenic, Matte Mousse
Would you like matching primer and setting spray? (Y/N): y
Recommended Primer: Mattifying, Oil-free, Water-based, Pore-Filling, Long Wearing
Recommended Setting Spray: Matte Finish Setting Sprays, Oil-Free Setting Sprays, Long-Wearing Setting Sprays, Oil-Control Setting Sprays, Mattifying Setting Sprays
The program will conclude with a message, "Enjoy your match!"


## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


Test with different skin types: "oily," "dry," "combination."
Test responses to primer and setting spray with "Y" and "N."
Test with invalid inputs (e.g., invalid skin type).
Test with mixed-case inputs.
Test with less common or unconventional skin types.

## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 


Unimplemented Features: While the current version provides personalized makeup recommendations based on skin type, I had initially planned to incorporate a feature for users to input specific skin concerns. This would enable the program to offer even more tailored recommendations, considering factors such as acne, dry patches, or redness.


Enhancements: One area for improvement is the refinement of the recommendation algorithm. With more time, I would explore machine learning techniques to enhance the accuracy of foundation suggestions. This could involve training a model on a broader dataset of makeup products and user preferences.


User Feedback Integration:As the project was developed independently, there wasn't an opportunity to gather direct user feedback. In the future, I would deploy the project and collect user responses to improve the user interface, address any usability issues, and fine-tune the recommendation engine based on real-world feedback.

Extended Functionality: I am keen on implementing computer vision to identify skin concerns visually. By integrating this technology, the Makeup Generator could offer a more comprehensive solution, suggesting not only suitable foundation types but also recommending skincare routines based on detected skin conditions.

Advanced Features: To further enhance the project, I would explore integrating with external APIs to fetch real-time data on makeup products. This would ensure that the recommendations are always up-to-date with the latest product offerings and advancements in the beauty industry.


## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

In the beginning, this course posed a significant challenge for me. I contemplated dropping it multiple times due to falling far behind in my work. However, after re-watching videos, reviewing the material, and seeking assistance whenever needed, I successfully navigated through the semester. I particularly relished the projects and group assignments we undertook in class. Working collaboratively in groups helped me learn more, and I also found value in watching instructional videos on YouTube. Through these activities, I finally grasped the concepts of Python, attained proficiency in writing code, and cultivated a better overall understanding of coding.

One thing I want to learn more about is how to implement computer vision to identify any skin concerns and generate a list of skincare routines for you. Additionally, I want to learn how to advance this project further in the future.
