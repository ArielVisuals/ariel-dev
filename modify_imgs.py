import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CECyT 12 image
content = content.replace(
    'src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=900&q=80"',
    'src="assets/cecyt12.jpeg"'
)

# Replace UPIITA image
content = content.replace(
    'src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80"',
    'src="assets/upiita.jpg"'
)

# Replace Freelance image
content = content.replace(
    'src="https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=900&q=80"',
    'src="assets/fiverr.webp"'
)

# Remove grayscale filter for Kreative Developer
# The img is:
# <img src="https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?auto=format&fit=crop&w=900&q=80" alt="Diseño de interfaces en equipo" loading="lazy" decoding="async">
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?auto=format&fit=crop&w=900&q=80" alt="Diseño de interfaces en equipo" loading="lazy" decoding="async">',
    '<img src="https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?auto=format&fit=crop&w=900&q=80" alt="Diseño de interfaces en equipo" loading="lazy" decoding="async" style="filter: none;">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
