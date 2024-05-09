{
    "name": "library app",
    "author": "Tarek Ashry",
    "summary": "The Library Module by Tarek Ashry is an essential tool for managing library resources efficiently.",
    "description": """
                   This is a dynamic application designed to streamline library operations and enhance user experience.
                   Developed by Tarek Ashry,
                   this module offers a sophisticated yet intuitive platform for librarians to manage their collections effectively.
                   With features tailored to meet the diverse needs of libraries,
                   it allows for easy cataloging, indexing, and tracking of library materials.
                   """,
    "category": "Productivity",
    "application": True,
    "data": [
        "data/data.xml",
        "data/cron.xml",
        "reports/book_print_template.xml",
        "reports/book_print.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/main_menu.xml",
        "views/book_view.xml",
        "views/publisher_view.xml",
        "views/sale_order_inherit_view.xml",
        "wizard/add_publisher_wizard.xml",
    ],
    "depends": ["base", "web", "sale_management", "mail"],
}
