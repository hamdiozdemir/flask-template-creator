from frontPy import TemplateCreator


# arg1 = ["Denemşğçe1.argüman\n", "Deneme 2.argümöşöçğsan\n", "Deneme 3.argüman\n"]

page = TemplateCreator("myPage")

page.start_navbar("MyApp", "#EA906C")
page.add_nav_item("Home", "#")
page.add_nav_item("Page One", "#page-one")
page.add_nav_item("Page TWO", "#page-two")
page.end_navbar()


page.start_section(height="80vh", class_name="main", background_color="red", padding="50px")

page.start_div(class_name="box", background_color="orange", width="200px", height="200px")

page.add_text("New Text to here.")
page.end_div()

page.end_section()

page.start_div(class_name="new-content", background_color="blue", padding="50px", border_radius="20px", border_type="solid", border_color="black")

page.start_div(background_color="gray")

page.start_div(width="300px", border_radius="30px", border_type="solid", background_color="orange", border_color="black", border_width="1px")
page.add_text("BOX ONE")
page.end_div()

page.start_div(width="300px", background_color="red", border_radius="30px", border_type="solid", border_color="black", border_width="1px")

page.add_text(text="""
    New Text is here,
    Another text one
    I keep adding...

""")
page.end_div()

page.end_div()


page.end_page()



