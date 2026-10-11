import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_backend.settings")
django.setup()

from portfolio.models import Project, Skill

def seed():
    Project.objects.all().delete()
    Skill.objects.all().delete()

    projects_data = [
        {
            "title": "Cravo Kitchen & Bar",
            "description": "A modern, responsive food ordering website and admin management platform for Cravo Kitchen & Bar, built with React 19, TypeScript, Tailwind CSS, Node.js, Express.js, and MySQL, with design DNA from Google Stitch AI.",
            "badges": ["React 19", "TypeScript", "Tailwind CSS", "Node.js", "Express.js", "MySQL", "JWT Auth", "REST API"],
            "features": [
                "Real-time Food Menu & Filters",
                "Interactive Cart & Checkout",
                "Live Kitchen Tickets Admin",
                "Dish Stock & Availability Toggle",
                "JWT Security & Rate Limiting",
                "Google Stitch AI Warm Epicurean UI"
            ],
            "architecture_steps": [
                "React 19 / TS Storefront",
                "Express.js REST Engine",
                "MySQL Connection Pool",
                "Live Kitchen Ticket Queue"
            ],
            "caseStudy": {
                "overview": "A modern, high-performance food ordering website and comprehensive administrative management platform engineered for Cravo Kitchen & Bar. The platform bridges customer storefront ordering with real-time kitchen operations, providing instantaneous dish search, dynamic cart calculations with free delivery thresholds, automated tax computations, and a secured JWT admin portal for live ticket tracking and menu management.",
                "problem": "Independent culinary venues frequently encounter heavy third-party marketplace commissions (up to 30%), clunky ordering experiences that cause customer abandonment, and an absence of direct, real-time ticket orchestration in the kitchen.",
                "solution": "Engineered a bespoke, commission-free fullstack restaurant solution with a client storefront boasting instant dish filtering, dynamic subtotal calculations, and streamlined checkout, alongside an authenticated administrative suite for live order status updates (Pending → Preparing → Ready → Delivered) and instant dish inventory toggling.",
                "features": "Features multi-category filtering (Burgers, Pizza, Chicken, Snacks, Drinks, Desserts), dynamic search, quantity adjustments, transparent delivery milestones (free delivery over $40), tax calculation (8.25%), kitchen dashboard with live metrics (Total Orders, Pending, Preparing, Ready, Delivered), and one-click stock toggle.",
                "architecture": "Decoupled architecture: Vite + React 19 + TypeScript frontend with Tailwind CSS and Lucide React, styled using Google Stitch AI's Warm Epicurean design tokens. Communicates via typed REST endpoints with a Node.js/Express backend, JWT token protection, bcrypt password hashing, and MySQL database persistence with auto-detecting embedded dev mode.",
                "technologies": "React 19, TypeScript, Vite, Tailwind CSS, React Router DOM v7, Node.js, Express.js, MySQL, JWT, bcryptjs, Lucide React, Google Stitch AI.",
                "challenges": "Synchronizing real-time order lifecycle changes across customer checkout and admin dashboard while upholding warm epicurean typography, responsive layout fluidity, and enterprise-grade input validation.",
                "result": "Deployed live to production at cravo-two.vercel.app with zero-configuration embedded resiliency, providing a premium dining experience and seamless kitchen operational efficiency."
            }
        },
        {
            "title": "E-Commerce Web Application",
            "description": "A full-stack e-commerce web application built using Python, Django, HTML, CSS, JavaScript and MySQL.",
            "badges": ["Python", "Django", "HTML", "CSS", "JavaScript", "MySQL", "REST API"],
            "features": [
                "User Authentication",
                "Product Catalog",
                "Order Management",
                "REST APIs",
                "Database Integration",
                "Responsive UI"
            ],
            "architecture_steps": [
                "Frontend (HTML/CSS/JS)",
                "Django REST API",
                "MySQL Database"
            ],
            "caseStudy": {
                "overview": "A comprehensive e-commerce platform designed to provide a seamless shopping experience. It handles everything from user registration to product browsing and order management.",
                "problem": "Traditional physical stores are limited by geography and business hours. Customers need a 24/7 accessible platform to browse and purchase products conveniently.",
                "solution": "Developed a full-stack web application with a responsive frontend for users and a robust Django backend to manage inventory, users, and orders securely.",
                "features": "Includes secure user authentication, dynamic product catalog, shopping cart functionality, order processing, and REST APIs for potential mobile app integration.",
                "architecture": "The application follows a client-server architecture. The frontend uses HTML/CSS/JS communicating with a Django REST API, which in turn reads and writes to a MySQL database.",
                "technologies": "Python, Django, HTML, CSS, JavaScript, MySQL, REST API.",
                "challenges": "Ensuring secure user authentication and designing a normalized database schema to handle products, users, and orders efficiently without redundancy.",
                "result": "A fully functional, responsive e-commerce platform capable of handling user registration, product browsing, and seamless order management."
            }
        },
        {
            "title": "AI Customer Support Chatbot",
            "description": "An AI-powered customer support chatbot using Natural Language Processing and Machine Learning.",
            "badges": ["Python", "Django", "Django REST Framework", "Scikit-learn", "NLP", "MySQL"],
            "features": [
                "Text Preprocessing",
                "Tokenization",
                "Intent Classification",
                "REST APIs",
                "External API Integration",
                "Context-aware Responses"
            ],
            "architecture_steps": [
                "User Message",
                "Text Preprocessing",
                "Tokenization",
                "Intent Classification",
                "Response Generation",
                "API Response"
            ],
            "caseStudy": {
                "overview": "An intelligent chatbot integrated into a web platform to assist users with common queries, significantly reducing the workload on human support agents.",
                "problem": "Customer support teams often spend a significant amount of time answering repetitive questions, leading to delayed response times for more complex issues.",
                "solution": "Implemented an AI-driven chatbot using Natural Language Processing (NLP) to understand user intents and provide immediate, context-aware responses.",
                "features": "Features text preprocessing, tokenization, intent classification using machine learning models, and a RESTful API for seamless integration with frontend interfaces.",
                "architecture": "User messages are sent to the Django backend via REST API. The backend preprocesses the text, tokenizes it, and feeds it into an ML classifier. The classified intent triggers the appropriate response generation.",
                "technologies": "Python, Django, Django REST Framework, Scikit-learn, NLP, MySQL.",
                "challenges": "Training the intent classification model with sufficient and diverse data to ensure high accuracy and handling edge cases where the bot doesn't understand the query.",
                "result": "A responsive chatbot capable of handling a wide variety of customer queries instantly, demonstrating the practical application of NLP in web services."
            }
        }
    ]

    for p_data in projects_data:
        Project.objects.create(
            title=p_data['title'],
            description=p_data['description'],
            badges=p_data['badges'],
            features=p_data['features'],
            architecture_steps=p_data['architecture_steps'],
            case_study_overview=p_data['caseStudy']['overview'],
            case_study_problem=p_data['caseStudy']['problem'],
            case_study_solution=p_data['caseStudy']['solution'],
            case_study_features=p_data['caseStudy']['features'],
            case_study_architecture=p_data['caseStudy']['architecture'],
            case_study_technologies=p_data['caseStudy']['technologies'],
            case_study_challenges=p_data['caseStudy']['challenges'],
            case_study_result=p_data['caseStudy']['result'],
        )

    skills_data = [
        {
            "category": "Frontend Development",
            "icon": "Layout",
            "items": ["React.js", "JavaScript", "HTML5", "CSS3"]
        },
        {
            "category": "Backend Development",
            "icon": "Server",
            "items": ["Python", "Django", "Flask", "Django REST Framework", "REST APIs"]
        },
        {
            "category": "Database",
            "icon": "Database",
            "items": ["MySQL", "SQLite", "SQL"]
        },
        {
            "category": "Data & AI",
            "icon": "BrainCircuit",
            "items": ["NumPy", "Pandas", "Matplotlib", "Scikit-learn", "Machine Learning", "NLP"]
        },
        {
            "category": "Tools",
            "icon": "Wrench",
            "items": ["Git", "GitHub"]
        }
    ]

    for s_data in skills_data:
        Skill.objects.create(
            category=s_data['category'],
            icon=s_data['icon'],
            items=s_data['items']
        )
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
