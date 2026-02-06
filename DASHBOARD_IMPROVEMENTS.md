# Dashboard Improvements

This document describes the recent improvements made to the GitHub Actions Dashboard.

## New Features

### 1. **Collapsible Projects**
Projects can now be collapsed and expanded to improve readability when monitoring many repositories:

- **Click on any project header** to toggle collapse/expand for that specific project
- **Expand All button**: Expands all projects at once to see all workflow details
- **Collapse All button**: Collapses all projects to see just the summary view
- **State persistence**: Your collapse/expand preferences are saved in browser localStorage and restored on page reload

### 2. **Status Summary Badges**
Each project header now displays a summary of workflow statuses:

- **✓ Green badge**: Shows count of successful workflows
- **✗ Red badge**: Shows count of failed workflows  
- **? Yellow badge**: Shows count of pending/unknown workflows

This gives you an at-a-glance view of each project's health without expanding it.

### 3. **Modern UI Design**

#### Visual Improvements
- **GitHub-inspired dark theme**: Modern, easy-on-the-eyes color scheme
- **Improved typography**: Better font choices and hierarchy
- **Enhanced spacing**: More breathing room between elements
- **Status badges**: Pill-shaped badges with color-coded statuses
- **Stale indicators**: Visual badges for workflows that haven't run recently

#### Interactive Elements
- **Smooth animations**: Transitions when collapsing/expanding
- **Hover effects**: Interactive feedback on clickable elements
- **Better button styling**: Modern, accessible buttons with clear hover states
- **Chevron icons**: Visual indicators showing expand/collapse state

### 4. **Responsive Design**
The dashboard now works better on different screen sizes:

- **Desktop (≥1200px)**: Optimized layout with 75% width
- **Tablet**: Adaptive layout at 90% width
- **Mobile (≤768px)**: Compact layout with adjusted font sizes and spacing

## Screenshots

### Fully Expanded View
All projects showing their complete workflow details:

![Expanded Dashboard](https://github.com/user-attachments/assets/49a2fe12-8345-4c1e-bfce-b64abfc791fb)

### Partially Collapsed View
Some projects collapsed to focus on specific ones:

![Partially Collapsed](https://github.com/user-attachments/assets/760fbd59-7ebc-4691-a799-481e910a846b)

### Fully Collapsed View
All projects collapsed for a high-level overview:

![All Collapsed](https://github.com/user-attachments/assets/63cf10a4-a1b9-43f6-80b3-49ce68a37d9e)

## Technical Details

### Files Modified

1. **`templates/dash_template.jinja`**
   - Restructured HTML with proper table grouping using `<tbody>`
   - Added JavaScript for interactive collapse/expand functionality
   - Implemented localStorage for state persistence
   - Added control buttons (Expand All / Collapse All)
   - Enhanced project headers with status summaries
   - Improved semantic HTML structure

2. **`html/css/styles.css`**
   - Complete redesign with modern color palette
   - GitHub-inspired dark theme (#0d1117, #161b22, etc.)
   - Gradient backgrounds for visual depth
   - Smooth transitions and hover effects
   - Responsive breakpoints for different screen sizes
   - Better spacing and typography

### Key Features Implementation

#### Collapsible Functionality
```javascript
function toggleProject(projectId) {
    // Toggle visibility of workflow rows
    // Update chevron icon direction
    // Save state to localStorage
}
```

#### State Persistence
The dashboard remembers which projects you've collapsed using browser localStorage. This means your preferences persist across:
- Page reloads
- Auto-refresh (every 60 seconds)
- Browser sessions (until you clear localStorage)

#### Status Badges
Uses Jinja2 filters to count workflow statuses:
```jinja
{% set success_count = project.other_workflows|selectattr('workflow_status', 'equalto', 'success')|list|length %}
```

## Usage Tips

1. **For Quick Overview**: Click "Collapse All" to see all projects with just their status summaries
2. **Focus on Specific Projects**: Collapse all, then expand only the projects you're interested in
3. **Monitor Changes**: The colored badges make it easy to spot failures (red) or pending builds (yellow)
4. **Mobile Monitoring**: The responsive design works well on phones for on-the-go monitoring

## Generating Example Dashboard

A Python script is included to generate an example dashboard with mock data:

```bash
python generate_example.py
```

This creates `example_dashboard.html` which you can open in a browser to see the improvements without needing GitHub API tokens.

## Browser Compatibility

The dashboard uses modern web standards and is compatible with:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

Features used:
- CSS Grid & Flexbox
- LocalStorage API
- ES6 JavaScript (arrow functions, const/let, template literals)
- Modern CSS (gradients, transitions, custom properties)

## Future Enhancement Ideas

Potential improvements for future iterations:
- Search/filter functionality
- Sort projects by status
- Customizable color themes
- Export status reports
- Workflow run history charts
- Email/Slack notifications integration
- Dark/light theme toggle
