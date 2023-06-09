from frontPy import TemplateCreator


# arg1 = ["Denemşğçe1.argüman\n", "Deneme 2.argümöşöçğsan\n", "Deneme 3.argüman\n"]

page = TemplateCreator("myPage")

page.start_navbar("MyApp", "#EA906C")
page.add_nav_item("Home", "#")
page.add_nav_item("Page One", "#page-one")
page.add_nav_item("Page TWO", "#page-two")
page.end_navbar()


page.start_section(height="80vh", background_color="red", padding="50px")
page.end_section()



page.end_page()



