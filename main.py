from agents import MarketingAnalysisAgents
from tasks import MarketingAnalysisTasks
from crewai import Crew
from dotenv import load_dotenv
load_dotenv()


tasks = MarketingAnalysisTasks()
agents = MarketingAnalysisAgents()

product_website = "https://seaiinitiative.github.io/SE.AI/"
product_details = "SE AI is pioneering the future of education with its state-of-the-art platform that integrates artificial intelligence and blockchain technology. This innovative solution is designed to transform learning experiences, making them more personalized, accessible, and secure. SE AI caters to a diverse range of learners, from students and professionals to educational institutions, by providing a customizable learning journey that meets the unique needs of each user. Features: 1. Personalized Learning Paths: Utilize AI-driven analytics to tailor educational content to the individual learning styles and pace of each user, enhancing understanding and retention. 2. Blockchain-Enabled Security: Securely store educational records and transactions on a blockchain, ensuring data integrity and easy verification of credentials without compromising privacy. 3. Interactive Learning Environments: Engage students with dynamic content including virtual reality classrooms and real-time problem-solving sessions, making learning not just informative but also immersive. 4. Decentralized Education System: Through blockchain, create a decentralized platform where users can access learning resources anytime, anywhere, breaking geographical and socio-economic barriers. 5. Continuous Assessment: AI algorithms provide ongoing assessments and feedback, allowing learners to gauge their progress and areas needing improvement continuously. 6. Gamification of Learning: Incorporate game mechanics to increase motivation and engagement through challenges, badges, and leaderboards. Benefits: - Enhanced Accessibility: SE AI makes high-quality education accessible to all, including underserved communities, by removing traditional barriers to learning. - Improved Engagement: Our gamified learning approach ensures that students are not just passive recipients of information but active participants in their education journey. - Lifetime Learning: From K-12 to professional development, SE AI supports lifelong learning, helping individuals stay relevant in an ever-changing global landscape. - Verifiable Credentials: Instantly verify educational achievements through a tamper-proof digital ledger, facilitating seamless transitions between learning stages and professional environments. Why SE AI? Choose SE AI for an education that's as dynamic as the world around us. Our platform not only educates but also inspires, prepares, and empowers learners to achieve their full potential. With SE AI, education is not just about knowledge transmission; it's about building a foundation for continual growth and success."

# Create Agents
product_competitor_agent = agents.product_competitor_agent()
strategy_planner_agent = agents.strategy_planner_agent()
creative_agent = agents.creative_content_creator_agent()
# Create Tasks
website_analysis = tasks.product_analysis(
    product_competitor_agent, product_website, product_details)
market_analysis = tasks.competitor_analysis(
    product_competitor_agent, product_website, product_details)
campaign_development = tasks.campaign_development(
    strategy_planner_agent, product_website, product_details)
write_copy = tasks.instagram_ad_copy(creative_agent)

# Create Crew responsible for Copy
copy_crew = Crew(
    agents=[
        product_competitor_agent,
        strategy_planner_agent,
        creative_agent
    ],
    tasks=[
        website_analysis,
        market_analysis,
        campaign_development,
        write_copy
    ],
    verbose=True,
    # Remove this when running locally. This helps prevent rate limiting with groq.
    max_rpm=1
)

ad_copy = copy_crew.kickoff()

# Create Crew responsible for Image
senior_photographer = agents.senior_photographer_agent()
chief_creative_diretor = agents.chief_creative_diretor_agent()
# Create Tasks for Image
take_photo = tasks.take_photograph_task(
    senior_photographer, ad_copy, product_website, product_details)
approve_photo = tasks.review_photo(
    chief_creative_diretor, product_website, product_details)

image_crew = Crew(
    agents=[
        senior_photographer,
        chief_creative_diretor
    ],
    tasks=[
        take_photo,
        approve_photo
    ],
    verbose=True,
    # Remove this when running locally. This helps prevent rate limiting with groq.
    max_rpm=1
)

image = image_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("Your post copy:")
print(ad_copy)
print("'\n\nYour midjourney description:")
print(image)
