from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Hardcoded data for portfolio
BLOGS_DATA = [
    {
        'id': 1,
        'title': "I don't need a stamp of MERN stack on my forehead",
        'excerpt': "A deep dive into why labeling yourself with technology stacks might limit your growth as a developer.",
        'content': """
        <p>In the fast-paced world of web development, it's easy to get caught up in the latest buzzwords and technology stacks. The MERN stack (MongoDB, Express.js, React, Node.js) has become incredibly popular, and many developers wear it like a badge of honor.</p>
        
        <p>But here's the thing - I don't need a stamp of MERN stack on my forehead to prove my worth as a developer. Technology is just a tool, and the best developers are those who can adapt and learn new tools as needed.</p>
        
        <p>What matters more is understanding fundamental programming concepts, problem-solving skills, and the ability to write clean, maintainable code. These skills transcend any particular technology stack.</p>
        
        <p>Instead of limiting myself to one stack, I prefer to think of myself as a full-stack developer who happens to know MERN, but is always ready to learn and work with new technologies that best solve the problem at hand.</p>
        """,
        'author': 'Buddhadeb Koner',
        'views': 48,
        'likes': 4,
        'date': '2024-06-01',
        'tags': ['Career', 'Development', 'MERN', 'Technology']
    },
    {
        'id': 2,
        'title': "C++ Compilation and Execution",
        'excerpt': "How to run C and C++ files in a proper way with modern tools and best practices.",
        'content': """
        <p>C++ remains one of the most powerful programming languages, but many beginners struggle with the compilation and execution process. Let me walk you through the proper way to compile and run C++ programs.</p>
        
        <h3>Basic Compilation</h3>
        <pre><code>g++ -o program program.cpp</code></pre>
        
        <h3>With Debugging Information</h3>
        <pre><code>g++ -g -o program program.cpp</code></pre>
        
        <h3>With Optimization</h3>
        <pre><code>g++ -O2 -o program program.cpp</code></pre>
        
        <p>Understanding these compilation flags will help you write better C++ code and debug issues more effectively. Always compile with warnings enabled using -Wall to catch potential issues early.</p>
        """,
        'author': 'Buddhadeb Koner',
        'views': 119,
        'likes': 17,
        'date': '2024-05-15',
        'tags': ['C++', 'Programming', 'Compilation', 'Tutorial']
    },
    {
        'id': 3,
        'title': "Building Scalable Web Applications with Next.js",
        'excerpt': "Learn how to build performant and scalable web applications using Next.js and modern React patterns.",
        'content': """
        <p>Next.js has revolutionized the way we build React applications by providing a full-stack framework with built-in optimizations and best practices.</p>
        
        <h3>Key Features</h3>
        <ul>
            <li>Server-Side Rendering (SSR)</li>
            <li>Static Site Generation (SSG)</li>
            <li>API Routes</li>
            <li>Automatic Code Splitting</li>
            <li>Image Optimization</li>
        </ul>
        
        <p>In this article, we'll explore how to leverage these features to build applications that are not only fast but also SEO-friendly and user-centric.</p>
        """,
        'author': 'Buddhadeb Koner',
        'views': 89,
        'likes': 12,
        'date': '2024-06-10',
        'tags': ['Next.js', 'React', 'SSR', 'Performance']
    }
]

PROJECTS_DATA = [
    {
        'id': 1,
        'title': 'Blog App',
        'description': 'Discover an engaging blog platform built with the MERN stack. Featuring a custom admin panel that enables administrators to create, update, and delete posts, this project seamlessly integrates with a MongoDB database for dynamic content delivery.',
        'detailed_description': """
        <p>This comprehensive blog application demonstrates my proficiency in full-stack development using the MERN stack. The project includes:</p>
        
        <h3>Features:</h3>
        <ul>
            <li>User authentication and authorization</li>
            <li>Admin panel for content management</li>
            <li>Rich text editor for blog posts</li>
            <li>Comment system with moderation</li>
            <li>Search functionality</li>
            <li>Responsive design</li>
        </ul>
        
        <h3>Technologies Used:</h3>
        <ul>
            <li>MongoDB for database</li>
            <li>Express.js for backend API</li>
            <li>React for frontend</li>
            <li>Node.js runtime</li>
            <li>JWT for authentication</li>
            <li>Cloudinary for image hosting</li>
        </ul>
        """,
        'technologies': ['MongoDB', 'Express.js', 'React', 'Node.js', 'JWT'],
        'github_url': 'https://github.com/buddhadebkoner/blog-app',
        'live_url': 'https://blog-app-demo.com',
        'image_url': '/static/images/blog-app.jpg',
        'status': 'Completed',
        'date': '2024-03-15'
    },
    {
        'id': 2,
        'title': 'URL Shortener',
        'description': 'In 24 hr I made it using Next.js — the URL shortener, and you can check the click and analytics of the URL. Check it out — you can modify and showcase it in your resume. Also, it\'s free for all.',
        'detailed_description': """
        <p>A lightning-fast URL shortening service built in just 24 hours using Next.js. This project showcases rapid prototyping skills and modern web development practices.</p>
        
        <h3>Features:</h3>
        <ul>
            <li>URL shortening with custom aliases</li>
            <li>Click tracking and analytics</li>
            <li>QR code generation</li>
            <li>Dashboard for URL management</li>
            <li>Rate limiting for abuse prevention</li>
            <li>Responsive design</li>
        </ul>
        
        <h3>Technologies Used:</h3>
        <ul>
            <li>Next.js 14 with App Router</li>
            <li>Prisma ORM</li>
            <li>PostgreSQL database</li>
            <li>Tailwind CSS</li>
            <li>Chart.js for analytics</li>
        </ul>
        """,
        'technologies': ['Next.js', 'Prisma', 'PostgreSQL', 'Tailwind CSS'],
        'github_url': 'https://github.com/buddhadebkoner/url-shortener',
        'live_url': 'https://short-url-demo.com',
        'image_url': '/static/images/url-shortener.jpg',
        'status': 'Completed',
        'date': '2024-05-20'
    },
    {
        'id': 3,
        'title': 'Social Media Website',
        'description': 'Kochu-Media is a modern social media platform designed to enhance online interaction through a feature-rich environment where users can post photos with captions, save posts, and engage with dynamic content.',
        'detailed_description': """
        <p>Kochu-Media is a comprehensive social media platform that rivals modern social networks with its rich feature set and engaging user experience.</p>
        
        <h3>Features:</h3>
        <ul>
            <li>User profiles and authentication</li>
            <li>Photo and video posting</li>
            <li>Real-time comments and likes</li>
            <li>Follow/unfollow system</li>
            <li>Story feature</li>
            <li>Direct messaging</li>
            <li>Search and discovery</li>
            <li>Content moderation</li>
        </ul>
        
        <h3>Technologies Used:</h3>
        <ul>
            <li>React with Redux for state management</li>
            <li>Express.js backend</li>
            <li>MongoDB with Mongoose</li>
            <li>Socket.io for real-time features</li>
            <li>Cloudinary for media storage</li>
            <li>Material-UI for components</li>
        </ul>
        """,
        'technologies': ['React', 'Redux', 'Express.js', 'MongoDB', 'Socket.io'],
        'github_url': 'https://github.com/buddhadebkoner/kochu-media',
        'live_url': 'https://kochu-media.com',
        'image_url': '/static/images/social-media.jpg',
        'status': 'In Development',
        'date': '2024-06-01'
    }
]

SKILLS_DATA = {
    'frontend': ['React', 'Next.js', 'JavaScript', 'TypeScript', 'HTML5', 'CSS3', 'Tailwind CSS', 'Material-UI'],
    'backend': ['Node.js', 'Express.js', 'Python', 'Django', 'Flask', 'RESTful APIs', 'GraphQL'],
    'database': ['MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Prisma ORM', 'Mongoose'],
    'tools': ['Git', 'Docker', 'Vercel', 'Netlify', 'AWS', 'Postman', 'VS Code', 'Linux'],
    'languages': ['JavaScript', 'TypeScript', 'Python', 'C++', 'Java', 'SQL']
}

EXPERIENCE_DATA = [
    {
        'id': 1,
        'company': 'Zidio',
        'position': 'Full Stack Developer Intern',
        'duration': 'Apr 2024 - Present',
        'status': 'Current',
        'description': 'Working on various web development projects using MERN stack. Collaborated with senior developers on client projects and gained experience in agile development methodologies.',
        'technologies': ['React', 'Node.js', 'MongoDB', 'Express.js'],
        'achievements': [
            'Developed 3 client projects from scratch',
            'Improved application performance by 40%',
            'Mentored 2 junior interns'
        ]
    },
    {
        'id': 2,
        'company': 'Freelance',
        'position': 'Web Developer',
        'duration': 'Jan 2024 - Present',
        'status': 'Ongoing',
        'description': 'Providing web development services to small businesses and startups. Specializing in responsive web design and full-stack applications.',
        'technologies': ['Next.js', 'React', 'Django', 'PostgreSQL'],
        'achievements': [
            'Completed 15+ projects',
            'Maintained 100% client satisfaction rate',
            'Generated $10K+ in revenue'
        ]
    }
]

def home(request):
    context = {
        'current_time': timezone.now().time(),
        'current_date': timezone.now().date(),
        'current_datetime': timezone.now(),
        'current_timezone': timezone.get_current_timezone(),
        'recent_blogs': BLOGS_DATA[:2],
        'featured_projects': PROJECTS_DATA[:3],
        'skills': SKILLS_DATA,
    }
    return render(request, 'website/index_new.html', context)

def about(request):
    context = {
        'skills': SKILLS_DATA,
        'experience': EXPERIENCE_DATA,
    }
    return render(request, 'website/about_tailwind_new.html', context)

def contact(request):
    return render(request, 'website/contact.html')

def blogs(request):
    context = {
        'blogs': BLOGS_DATA,
        'page_title': 'All Blogs'
    }
    return render(request, 'website/blogs.html', context)

def blog_detail(request, blog_id):
    blog = next((blog for blog in BLOGS_DATA if blog['id'] == blog_id), None)
    if not blog:
        return HttpResponse("Blog not found", status=404)
    
    context = {
        'blog': blog,
        'related_blogs': [b for b in BLOGS_DATA if b['id'] != blog_id][:2]
    }
    return render(request, 'website/blog_detail.html', context)

def projects(request):
    context = {
        'projects': PROJECTS_DATA,
        'page_title': 'All Projects'
    }
    return render(request, 'website/projects.html', context)

def project_detail(request, project_id):
    project = next((project for project in PROJECTS_DATA if project['id'] == project_id), None)
    if not project:
        return HttpResponse("Project not found", status=404)
    
    context = {
        'project': project,
        'related_projects': [p for p in PROJECTS_DATA if p['id'] != project_id][:2]
    }
    return render(request, 'website/project_detail.html', context)

def skills(request):
    context = {
        'skills': SKILLS_DATA,
        'page_title': 'Skills & Technologies'
    }
    return render(request, 'website/skills.html', context)

def experience(request):
    context = {
        'experience': EXPERIENCE_DATA,
        'page_title': 'Work Experience'
    }
    return render(request, 'website/experience.html', context)

def resume(request):
    context = {
        'skills': SKILLS_DATA,
        'experience': EXPERIENCE_DATA,
        'projects': PROJECTS_DATA,
        'education': [
            {
                'degree': 'Bachelor of Technology in Computer Science',
                'institution': 'University of Engineering & Management',
                'year': '2022 - 2026',
                'cgpa': '8.5/10'
            }
        ]
    }
    return render(request, 'website/resume.html', context)