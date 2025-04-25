# Portfolio Website Technical Design Document (Revised)

## 1. Project Overview

A responsive portfolio website to showcase professional skills and projects with a clean, modern design.

## 2. Requirements

- Responsive design for desktop and mobile devices
- Navigation bar with sections: About, Projects, and Skills
- Manual project showcase
- Clean project structure with separated HTML, CSS, and JavaScript files
- Use Tailwind CSS via CDN (no npm build process)

## 3. Technology Stack

- **HTML5**: Core structure
- **Tailwind CSS (CDN)**: Styling framework
- **JavaScript**: Dynamic content and interactions (minimal use)

## 4. Project Structure

```
portfolio-site/
├── index.html              # Main HTML structure
├── css/
│   └── styles.css          # Custom styles beyond Tailwind
├── js/
│   └── main.js             # JavaScript functionality (navigation, etc.)
└── images/
    ├── profile.jpg         # Profile picture
    └── projects/           # Project screenshots
        ├── project1.jpg
        ├── project2.jpg
        └── ...
```

## 5. Component Design

### 5.1 Navigation Bar
- Fixed position at top
- Responsive design: horizontal menu on desktop, hamburger menu on mobile
- Smooth scrolling to sections
- Active section highlighting

### 5.2 About Section
- Profile picture
- Name and professional title
- Brief introduction
- Social links (GitHub, LinkedIn, etc.)

### 5.3 Skills Section
- Visual representation of technical skills
- Categories (Frontend, Backend, Tools, etc.)
- Skill level indicators or tags

### 5.4 Projects Section
- Manually created project cards
- Project details: title, description, technologies used, links
- Screenshots for each project
- Consistent card layout for all projects

### 5.5 Footer
- Contact information
- Copyright information
- Additional links

## 6. Tailwind CSS Implementation (CDN)

### 6.1 Setup Process
1. Add Tailwind CSS CDN to HTML header:
   ```html
   <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
   ```
   
   Alternatively, use the script CDN:
   ```html
   <script src="https://cdn.tailwindcss.com"></script>
   ```

2. Create a custom CSS file for additional styles:
   ```
   /css/styles.css
   ```

### 6.2 Limitations of CDN Approach
- No PurgeCSS optimization (larger file size)
- Limited customization of Tailwind configuration
- No custom plugins

### 6.3 Custom CSS Extensions
- Create a separate CSS file for styles beyond Tailwind
- Use CSS custom properties for consistent theming
- Maintain a modular approach to styling

## 7. Responsive Design Strategy

### 7.1 Breakpoints
Using Tailwind's default breakpoints:
- Mobile: < 640px (`sm`)
- Tablet: 640px - 1024px (`md` to `lg`)
- Desktop: > 1024px (`lg` and above)

### 7.2 Design Approach
- Mobile-first development
- Flexible grid layouts using Tailwind's grid system
- Strategic use of flexbox for alignment
- Appropriate spacing adjustments across breakpoints
- Use of Tailwind's responsive prefixes (e.g., `md:flex`)

## 8. Manual Project Showcase

### 8.1 Project Card Structure
```html
<div class="bg-white rounded-lg shadow overflow-hidden hover:shadow-lg transition-shadow duration-300">
  <div class="project-image">
    <img src="./images/projects/project1.jpg" alt="Project Name" class="w-full h-48 object-cover">
  </div>
  <div class="p-6">
    <h3 class="text-xl font-bold mb-2">Project Name</h3>
    <p class="text-gray-600 mb-4">Project description goes here...</p>
    <div class="flex flex-wrap gap-2 mb-4">
      <span class="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded">HTML</span>
      <span class="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded">CSS</span>
      <span class="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded">JavaScript</span>
    </div>
    <div class="flex gap-4">
      <a href="#" target="_blank" class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors">Live Demo</a>
      <a href="#" target="_blank" class="px-4 py-2 border border-gray-300 rounded hover:bg-gray-50 transition-colors">Source Code</a>
    </div>
  </div>
</div>
```

### 8.2 Project Data Structure
- Each project will include:
  - Title
  - Description
  - Screenshot
  - Technologies used
  - Links to live demo and source code
  - Optional: date, role, challenges solved

## 9. JavaScript Functionality

### 9.1 Mobile Navigation
```javascript
// Toggle mobile menu
const menuButton = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

menuButton.addEventListener('click', () => {
  mobileMenu.classList.toggle('hidden');
});
```

### 9.2 Smooth Scrolling
```javascript
// Smooth scroll to sections
document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
    
    // Close mobile menu if open
    if (!mobileMenu.classList.contains('hidden')) {
      mobileMenu.classList.add('hidden');
    }
  });
});
```

### 9.3 Active Section Highlighting
```javascript
// Highlight active section in navigation
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('nav a[href^="#"]');
  
  let currentSection = '';
  
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= sectionTop - 60) {
      currentSection = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.classList.remove('text-blue-500');
    link.classList.add('text-gray-600');
    if (link.getAttribute('href') === `#${currentSection}`) {
      link.classList.remove('text-gray-600');
      link.classList.add('text-blue-500');
    }
  });
});
```

## 10. Implementation Plan

### Phase 1: Setup & Structure
- Create project folder structure
- Set up HTML with Tailwind CSS CDN
- Create basic HTML structure with appropriate sections

### Phase 2: Core Components
- Implement navigation bar with mobile responsiveness
- Build About section with profile info
- Create Skills section with visual representation

### Phase 3: Projects Section
- Design project card template
- Create sample project entries
- Implement card layout and responsiveness

### Phase 4: Responsive Design
- Test across devices
- Refine mobile navigation
- Adjust spacing and typography for different screens

### Phase 5: Refinement
- Add subtle animations/transitions
- Implement custom styling touches
- Optimize images
- Test browser compatibility

## 11. Additional Considerations

### 11.1 Accessibility
- Semantic HTML elements (`header`, `nav`, `main`, `section`, `footer`)
- ARIA attributes where needed
- Keyboard navigation support
- Sufficient color contrast (min 4.5:1 for text)
- Focus states for interactive elements

### 11.2 SEO
- Proper meta tags in the `<head>`
- Descriptive alt text for all images
- Semantic heading structure (h1, h2, h3)
- Canonical URL

### 11.3 Performance
- Compress and optimize images
- Use appropriate image sizes/formats
- Minify custom JavaScript
- Consider lazy loading for project images

This technical design document provides a comprehensive framework for developing a professional portfolio website with a clean, modular structure using Tailwind CSS via CDN instead of npm, making the setup process simpler while still maintaining a responsive and visually appealing design.