Getting Started
===============

This guide explains how to install and run HealthHabitHelper.

1. Prerequisites
----------------

* Python 3.8+
* Git

2. Installation and Setup
-------------------------

Clone the repository and install dependencies.

.. code-block:: bash

   git clone https://github.com/YulGod/HealthHabitHelper.git
   cd HealthHabitHelper
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\\Scripts\\activate  # Windows
   pip install -r requirements.txt

3. Running the Application
--------------------------

Start the Flask server to access the application via your web browser.

.. code-block:: bash

   # Command to run the Flask application
   python app.py