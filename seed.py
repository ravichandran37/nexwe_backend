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
            "title": "Catchy Exports",
            "description": "A modern, cinematic, high-converting B2B fruit export landing page engineered for Catchy Exports to serve wholesale fruit importers, supermarket chains, and distribution desks worldwide.",
            "badges": ["HTML5", "Tailwind CSS", "GSAP 3", "ScrollTrigger", "Vanilla JS", "Phosphor Icons", "B2B Export"],
            "features": [
                "B2B Wholesale RFQ Portal",
                "Cold-Chain Logistics Specs",
                "Interactive GSAP Showcase"
            ],
            "architecture_steps": [
                "Semantic HTML5 Shell",
                "Tailwind Utility Framework",
                "GSAP 3 ScrollTrigger Engine",
                "Interactive RFQ Modal & Storage"
            ],
            "caseStudy": {
                "overview": "A modern, cinematic, high-converting B2B fruit export landing page engineered for Catchy Exports to serve wholesale fruit importers, supermarket chains, and distribution desks worldwide. Built with pure semantic HTML5, tailored Tailwind CSS styling, GSAP 3 scroll animations, and interactive quote inquiry workflows.",
                "problem": "Traditional agricultural export websites suffer from dated designs, lack of clear technical trade specifications, friction-filled inquiry processes, and poor mobile responsiveness, leading to missed opportunities with international B2B buyers.",
                "solution": "Developed a high-converting, performance-driven digital presence featuring a cinematic emerald aesthetic, interactive character-split headline animations, an interactive 3-panel horizontal pin-scroll product showcase, an automated testimonial carousel, and an interactive glassmorphic RFQ (Request for Quote) system with instant client validation and reference codes.",
                "features": "Features character-by-character headline splitting, interactive preloader (0-100% progress), subtle magnetic CTA buttons, 3-panel horizontal showcase for export fruits (Alphonso Mangoes, Bananas, Cold-Chain Fleet), automatic client testimonial slider, and a modal-grade B2B inquiry/RFQ form with validation and reference generation.",
                "architecture": "Self-contained frontend architecture powered by semantic HTML5, modern utility-first Tailwind CSS, and hardware-accelerated GSAP 3 with ScrollTrigger plugins. Centralized business configuration model provides instant zero-build customization, while respecting user accessibility preferences (prefers-reduced-motion).",
                "technologies": "HTML5, Tailwind CSS, GSAP 3, GSAP ScrollTrigger, Vanilla JavaScript (ES6+), Phosphor Icons, Google Fonts (Space Grotesk & Outfit), Vercel.",
                "challenges": "Engineering smooth horizontal pin-scroll mechanics on desktop that gracefully fold down into a natural vertical stack on touch devices, all while maintaining zero-dependency build architecture and sub-second load times.",
                "result": "Deployed live to production at catchyexports.vercel.app with flawless responsiveness across all viewports from 320px to 4K displays, establishing an authoritative international brand identity for wholesale fruit exports."
            }
        },
        {
            "title": "AURA // Street × Heritage",
            "description": "A high-concept, editorial e-commerce platform and digital brand world designed for a contemporary Indian luxury streetwear label marrying artisanal textiles with modern silhouettes.",
            "badges": ["HTML5", "Tailwind CSS", "GSAP 3", "ScrollTrigger", "Vanilla JS", "Phosphor Icons", "E-Commerce"],
            "features": [
                "Interactive Cart & Checkout",
                "Parallax Lookbook & Stories",
                "Interactive India Craft Map"
            ],
            "architecture_steps": [
                "Editorial HTML5 Layout",
                "Reactive Vanilla Cart Store",
                "GSAP Parallax Scroll Timeline",
                "Interactive Regional SVG Craft Map"
            ],
            "caseStudy": {
                "overview": "Aura is a high-concept, editorial e-commerce platform and digital brand world designed for a contemporary Indian luxury streetwear label. It marries traditional Indian artisanal textiles (Khadi, Jamdani, Ikat) with modern oversize streetwear silhouettes, featuring a slide-out cart drawer, interactive India craft map, parallax lookbook, story reader modal, and interactive checkout flow.",
                "problem": "High-end fashion consumers demand immersive, narrative-driven shopping experiences that transcend static product grids. Traditional Shopify or generic e-commerce templates fail to communicate cultural authenticity, fabric provenance, and the rebellious spirit of modern urban fashion.",
                "solution": "Engineered a cinematic, editorial digital storefront utilizing custom GSAP scroll timelines, an interactive craft map exploring regional textile hubs (Varanasi, Kutch, Pochampally), a full-featured slide-out cart drawer with dynamic subtotal & discount calculation, product quick-view modals, and simulated frictionless checkout.",
                "features": "Interactive 0–100% preloader, sticky editorial navbar with search and slide-out cart drawer, multi-category collection filtering (Overshirts, Hoodies, Cargos, Accessories), size selectors with real-time stock indicators, interactive SVG India craft map with clickable cultural hubs, parallax lookbook, and interactive story reader modal.",
                "architecture": "High-performance modular architecture built with semantic HTML5, utility-first Tailwind CSS, and hardware-accelerated GSAP 3 & ScrollTrigger. State management for cart items, promo codes, search indexing, and modal lifecycle is driven by reactive Vanilla JavaScript with persistent localStorage caching.",
                "technologies": "HTML5, Tailwind CSS, GSAP 3, GSAP ScrollTrigger, Vanilla JavaScript (ES6+), Phosphor Icons, Google Fonts (Syne & Manrope), Vercel.",
                "challenges": "Harmonizing rich editorial animations and interactive SVG mapping with instantaneous page responsiveness, touch-friendly gestures, and accessible keyboard navigation without relying on heavy third-party UI frameworks.",
                "result": "Deployed live to production at aura-virid-eta.vercel.app, delivering a seamless 60fps luxury shopping experience that establishes an unforgettable digital benchmark for contemporary Indian streetwear."
            }
        },
        {
            "title": "Studio Kanso",
            "description": "A bespoke, production-ready website for an interior architecture and spatial design studio, crafted with Next.js App Router, React 19, TypeScript, Tailwind CSS, GSAP motion, Sanity CMS, and Resend.",
            "badges": ["Next.js 16", "React 19", "TypeScript", "Tailwind CSS v4", "GSAP 3", "Sanity CMS", "Resend API", "Zod"],
            "features": [
                "Tactile Material Explorer",
                "Interactive Project Lightbox",
                "Headless Sanity CMS & Resend"
            ],
            "architecture_steps": [
                "Next.js App Router & SSR",
                "GSAP Kinetic Scroll Engine",
                "Sanity Headless Content Lake",
                "Zod & Resend Dispatch"
            ],
            "caseStudy": {
                "overview": "Studio Kanso is a bespoke, production-ready digital atelier engineered for a luxury interior architecture and spatial design studio. Founded on wabi-sabi modernism and tactile materiality, the platform features dynamic architectural reveals, a tactile material explorer, interactive commission case studies with accessible lightboxes, headless Sanity Studio content synchronization, and server-validated consultation dispatch.",
                "problem": "High-end architectural ateliers require digital experiences that mirror the tactile, restrained luxury of physical spaces. Standard website templates rely on generic grids, lack visceral typography, fail to highlight material provenance (travertine, slaked lime, smoked oak), and lack robust headless CMS workflows for architectural portfolios.",
                "solution": "Engineered an editorial, high-performance web experience leveraging Next.js App Router, React 19, and Tailwind CSS v4 paired with Cormorant Garamond and Manrope typography. Integrated GSAP 3 scroll animations, an interactive Materiality Explorer, before/after renovation sliders, dual-mode embedded demo datasets with headless Sanity Studio, and server-validated consultation inquiries via Resend.",
                "features": "Architectural hero with clip-path reveal, interactive portfolio filtering (Residential, Commercial, Hospitality, Villas, Apartments), full commission case studies with finish schedules & before/after sliders, Tactile Material Explorer, pinned 4-phase process sequence, Sanity Studio mounted at /cms, sliding-window rate limiting, and WhatsApp direct studio chat generation.",
                "architecture": "Modern full-stack SSR/SSG architecture built with Next.js 16 App Router, React 19, TypeScript, and Tailwind CSS v4. Content orchestration is backed by Sanity CMS schemas with automatic high-fidelity fallback to embedded demo content. API routes enforce strict Zod validation, honeypot spam protection, and transactional notification dispatch via Resend.",
                "technologies": "Next.js 16, React 19, TypeScript, Tailwind CSS v4, GSAP 3, Sanity CMS, Resend, React Hook Form, Zod, Cormorant Garamond, Vercel.",
                "challenges": "Balancing rich full-bleed imagery and buttery 60fps GSAP kinetic scroll interactions with strict Core Web Vitals, sub-second initial load times, and ensuring zero mock stub artifacts during offline or Sanity API transitions.",
                "result": "Deployed live to production at studio-kanso.vercel.app with immaculate responsive performance, establishing a benchmark digital presence for luxury interior architecture and bespoke spatial design."
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
