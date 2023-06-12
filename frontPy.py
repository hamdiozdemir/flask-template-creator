import os
import string
import random


class TemplateCreator():
    """A HTML and CSS template creator class."""

    def __init__(self, template_name):
        """Class gets a template names by default to create a html and css file with the name."""
        self.template_name = template_name
        self.html_content = f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename = '{self.template_name}.css') }}">
    <link rel="stylesheet" href="/static/{self.template_name}.css">

    <title>{self.template_name}</title>
</head>
<body>
        """
        
        self.html_content_end = """
</body>
</html>
        """
        
        self.css_content = """
*{
top: 0;
left: 0;
margin: 0;
}

        """

    def attr_name_generator(self):
        """Randomly generate attribute name."""
        chars = string.ascii_lowercase
        letters = []
        for index in range(len(chars)):
            letters.append(chars[index])
        
        attr_name = "".join(random.choices(letters, k=8))
        return attr_name



    def end_page(self):
        """Ends and create HTML and CSS files for page."""

        self.html_content += self.html_content_end

        if not os.path.exists("templates"):
            os.makedirs("templates")
        with open(f"templates/{self.template_name}.html", "w", encoding="utf-8") as file:
            file.write(self.html_content)
        
        if not os.path.exists("static"):
            os.makedirs("static")
        with open (f"static/{self.template_name}.css", "w", encoding="utf-8") as file:
            file.write(self.css_content)
        

    def start_navbar(self, title="MyApp", bg_color=None, position="fixed"):
        """Create / initialize navbar"""

        allowed_positions = ["fixed", "fixed-top", "fixed-bottom", "sticky-top", "sticky-bottom"]
        if position not in allowed_positions:
            raise ValueError(f'Invalid value for position. You can only use {", ".join(allowed_positions)} ')

        if bg_color:
            bg_color = f"style='background-color: {bg_color};'"
        else:
            bg_color = ""
        self.navbar_content = f"""
    <nav class="navbar navbar-expand-lg {position} bg-body-tertiary" {bg_color}>
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
                """
        return self.navbar_content
        
    def add_nav_item(self, title, link):
        """Add pages, headers to navbar"""

        self.navbar_content += f"""
    <li class="nav-item">
      <a class="nav-link active" aria-current="page" href="{link}">{title}</a>
    </li>
        """
        return self.navbar_content
    
    def end_navbar(self):
        """End and add the item to navbar"""


        self.navbar_content += """
      </ul>
    </div>
  </div>
</nav>
        """
        self.html_content += self.navbar_content
        return self.navbar_content
        
    def start_section(
            self,
            id="",
            class_name=None,
            height="100vh",
            width="100%",
            background_color="white",
            row_position="center",
            column_position="center",
            font_size="1rem",
            flex_wrap="nowrap",
            direction="row",
            gap="10px",
            padding="10px",
            border_width="0px",
            border_color="None",
            border_type="",
            border_radius="0px",
            ):
        """Start to create a section."""


        # argument checks

        position_check_list = ["center", "baseline", "end", "flex-end", "flex-start", "left", "right", "space-around", "space-between"]

        if row_position not in position_check_list or \
            column_position not in position_check_list:
            raise ValueError(f'Invalid value for position. You can only use {", ".join(position_check_list)} ')

        for arg in [height,width, gap, padding, border_width, border_radius]:
            if not arg.endswith(('px', '%', 'vh', 'vw')):
                raise ValueError(f"{arg} argument must be a number and ends with 'px', '%', 'vh', 'vw', 'rem' " )

        if not class_name:
            class_name = self.attr_name_generator()

        self.html_content += f"""
        <section class="{class_name}" id="{id}">
        """

        self.css_content += f"""      
.{class_name}{{
background: {background_color};
height: {height};
width: {width};
display: flex;
flex-direction: {direction};
flex-wrap: {flex_wrap};
gap: {gap};
align-items: {column_position};
justify-content: {row_position};
font-size: {font_size};
padding: {padding};
border: {border_width} {border_type} {border_color};
border-radius: {border_radius};

}}
        """

    def end_section(self):
        """Ends the section."""

        self.html_content += """
        </section>
        """
        return self.html_content
        
        
    def start_div(
            self,
            id="",
            class_name=None,
            width="100%",
            height="auto",
            background_color="white",
            row_position="center",
            column_position="center",
            font_size="1rem",
            flex_wrap="nowrap",
            direction="row",
            gap="10px",
            padding="10px",
            border_width="0px",
            border_color="None",
            border_type="",
            border_radius="0px",
            ):
        """Starts a div element."""

        position_check_list = ["center", "baseline", "end", "flex-end", "flex-start", "left", "right", "space-around", "space-between"]

        if row_position not in position_check_list or \
            column_position not in position_check_list:
            raise ValueError(f'Invalid value for position. You can only use {", ".join(position_check_list)} ')

        if not class_name:
            class_name = self.attr_name_generator()

        self.html_content += f"""
        <div class="{class_name}" id="{id}">
        """

        self.css_content += f"""      
.{class_name}{{
background: {background_color};
height: {height};
width: {width};
display: flex;
flex-direction: {direction};
flex-wrap: {flex_wrap};
gap: {gap};
align-items: {column_position};
justify-content: {row_position};
font-size: {font_size};
padding: {padding};
border: {border_width} {border_type} {border_color};
border-radius: {border_radius};

}}
        """

    def end_div(self):
        """Ends the div element."""

        self.html_content += """
        </div>
        """
        return self.html_content
    
    def add_text(self, text):
        """Add text to html content"""

        self.html_content += text
        return self.html_content

