# Dashboard Improvements

This document describes the improvements made to the GitHub Actions Dashboard.

## New Features (Phase 1: Collapsible Projects)

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

## New Features (Phase 2: Filters and Statistics)

### 5. **Statistics Panel**
A comprehensive overview panel displays aggregate statistics across all projects:

- **Total Projects**: Count of repositories being monitored
- **Total Workflows**: Sum of all workflows across all projects
- **Success Count**: Total successful workflow runs (green)
- **Failure Count**: Total failed workflow runs (red)
- **Pending Count**: Total pending/in-progress workflows (yellow)
- **Stale Count**: Total workflows that haven't run recently (gray)

Each statistic is presented in a color-coded card for quick visual scanning.

### 6. **Search Filter**
Real-time text search to filter projects by name:

- **Type to filter**: Instantly filters the project list as you type
- **Case-insensitive**: Matches regardless of letter casing
- **Substring matching**: Finds projects containing the search term anywhere in the name
- **Live counter**: Shows "X of Y projects" matching your search

Example: Type "wallet" to see only "cardano-wallet" and "cf-identity-wallet" projects.

### 7. **Status Filter**
Filter projects based on their workflow statuses:

- **All**: Shows all projects (default)
- **Healthy (no failures)**: Only projects with zero failed workflows
- **Has Failures**: Only projects with at least one failed workflow
- **Has Success**: Only projects with at least one successful workflow
- **Has Pending**: Only projects with at least one pending workflow

Use this to quickly focus on problematic projects or verify healthy ones.

### 8. **Sort Functionality**
Organize projects in different ways:

- **Name (A-Z)**: Alphabetical sort by project name (default)
- **Name (Z-A)**: Reverse alphabetical sort
- **Most Failures**: Projects with the most failures appear first

Sorting helps you prioritize which projects need attention.

### 9. **Combined Filters**
All filters work together seamlessly:

- **Search + Status**: Find specific projects with certain statuses
- **Search + Sort**: Find and organize matching projects
- **Status + Sort**: Focus on problematic projects sorted by severity

Example: Search for "cardano", filter by "Has Failures", sort by "Most Failures"

### 10. **Clear Filters Button**
One-click reset to remove all active filters:

- Clears search text
- Resets status filter to "All"
- Resets sort to "Name (A-Z)"
- Removes filter state from localStorage
- Shows all projects again

### 11. **Filter Persistence**
Filter preferences are saved and restored:

- **localStorage persistence**: Filters survive page reloads and auto-refresh
- **Automatic restoration**: Returns to your last filter settings
- **Per-browser storage**: Each browser maintains its own filter state

This ensures you don't lose your view when the dashboard auto-refreshes every 60 seconds.

## Screenshots

### Full Dashboard with Statistics and Filters
Complete view showing all new features:

![Dashboard with Filters](https://github.com/user-attachments/assets/ba4d4fc3-b351-438a-9321-1a0bcb590edb)

### Search Filter in Action
Filtering projects by name ("wallet"):

![Search Filter](https://github.com/user-attachments/assets/83f1ec08-a97b-42e2-a58e-6984ba14491a)

### Status Filter
Showing only projects with failures:

![Status Filter](https://github.com/user-attachments/assets/0ab0ce77-ebf9-462c-9c2b-ae09fb3d9337)

## Technical Details

### Files Modified

1. **`templates/dash_template.jinja`**
   - **Phase 1**: Restructured HTML with proper table grouping using `<tbody>`
   - Added JavaScript for interactive collapse/expand functionality
   - Implemented localStorage for state persistence
   - Added control buttons (Expand All / Collapse All)
   - Enhanced project headers with status summaries
   - Improved semantic HTML structure
   - **Phase 2**: Added statistics panel with Jinja2 calculations
   - Added filter panel with search input, status dropdown, and sort dropdown
   - Implemented JavaScript filter and sort functions
   - Added filter state persistence in localStorage

2. **`html/css/styles.css`**
   - **Phase 1**: Complete redesign with modern color palette
   - GitHub-inspired dark theme (#0d1117, #161b22, etc.)
   - Gradient backgrounds for visual depth
   - Smooth transitions and hover effects
   - Responsive breakpoints for different screen sizes
   - Better spacing and typography
   - **Phase 2**: Styled statistics panel with stat cards
   - Styled filter panel with inputs, selects, and buttons
   - Added color-coded stat numbers (success=green, failure=red, etc.)
   - Enhanced responsive design for new components

### Key Features Implementation

#### Collapsible Functionality (Phase 1)
```javascript
function toggleProject(projectId) {
    // Toggle visibility of workflow rows
    // Update chevron icon direction
    // Save state to localStorage
}
```

#### State Persistence
The dashboard remembers which projects you've collapsed and which filters you've applied using browser localStorage. This means your preferences persist across:
- Page reloads
- Auto-refresh (every 60 seconds)
- Browser sessions (until you clear localStorage)

#### Statistics Calculation (Phase 2)
Uses Jinja2 template logic to calculate aggregate statistics:
```jinja
{% set total_workflows = namespace(count=0) %}
{% for project in all_projects %}
    {% set total_workflows.count = total_workflows.count + project.other_workflows|length %}
{% endfor %}
```

#### Filtering Logic (Phase 2)
```javascript
function filterProjects() {
    // Get search term and status filter
    // Match against project name and status badges
    // Show/hide matching projects
    // Update result counter
    // Save filter state to localStorage
}
```

#### Sorting Logic (Phase 2)
```javascript
function sortProjects(criteria) {
    // Extract project groups and workflow bodies
    // Sort based on criteria (name or failure count)
    // Re-insert in sorted order
}
```

#### Status Badges (Phase 1)
Uses Jinja2 filters to count workflow statuses:
```jinja
{% set success_count = project.other_workflows|selectattr('workflow_status', 'equalto', 'success')|list|length %}
```

## Usage Tips

### For Quick Overview
1. **Collapse All** to see all projects with just their status summaries
2. Use the **Statistics Panel** to see aggregate counts at a glance
3. **Filter by "Has Failures"** to focus only on problematic projects

### For Focused Monitoring
1. **Search** for specific projects by name
2. **Sort by "Most Failures"** to prioritize problem areas
3. **Collapse all**, then expand only the projects you're interested in

### For Problem Resolution
1. **Filter by "Has Failures"** to see only projects with issues
2. **Sort by "Most Failures"** to see worst offenders first
3. Click on project headers to expand and see which specific workflows failed
4. Click on timestamps to go directly to the workflow run in GitHub

### For Status Reporting
1. Check the **Statistics Panel** for overall health metrics
2. **Filter by "Healthy"** to verify which projects are working well
3. Take note of **Stale** count to see which workflows need attention
4. Use **Search** to quickly find specific project status

## Generating Example Dashboard

A Python script is included to generate an example dashboard with mock data:

```bash
python generate_example.py
```

This creates `example_dashboard.html` which you can open in a browser to see all the improvements without needing GitHub API tokens.

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
- Array methods (filter, map, sort, forEach)

## Future Enhancement Ideas

Potential improvements for future iterations:
- **Advanced Filtering**: Filter by multiple statuses at once, date range filters
- **Workflow Details**: Show duration, triggering user, commit info
- **Charts & Graphs**: Visual trend analysis, failure rate over time
- **Customization**: User-configurable dashboard layout, column visibility
- **Notifications**: Email/Slack alerts for new failures
- **Export**: Download reports as CSV/PDF
- **Dark/Light Theme Toggle**: User preference for color scheme
- **Workflow Run History**: Show recent runs in a timeline
- **Multi-Repository Groups**: Organize related repositories together
- **Quick Actions**: Retry failed workflows, approve pending runs directly from dashboard
