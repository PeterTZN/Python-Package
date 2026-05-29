from setuptools import setup

setup(
    name='invoice4pdf',
    packages=['invoicing'],
    version='1.0.0',
    license='MIT',
    description='A Python package that automates the conversion of Excel spreadsheet invoices into professionally formatted PDF documents, complete with itemised tables, calculated totals, and company branding.',
    long_description="""
invoice4pdf is a lightweight Python package that streamlines invoice generation 
for small businesses and developers. Simply provide Excel (.xlsx) invoice files 
named with an invoice number and date, and the package automatically produces 
clean, formatted PDF invoices — complete with itemised product tables, unit 
prices, quantities, line totals, a calculated grand total, and your company logo.

Key Features:
- Batch processes multiple Excel invoice files in one run
- Extracts invoice number and date directly from the filename
- Generates a professionally formatted PDF per invoice
- Calculates and displays grand totals automatically
- Supports company logo branding
    """,
    long_description_content_type='text/plain',
    author='Peter Thomson',
    author_email='your.email@example.com',
    url='https://github.com/PeterTZN/Python-Package',
    keywords=['invoice', 'excel', 'pdf', 'automation', 'billing'],
    install_requires=['pandas', 'fpdf2', 'openpyxl'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.13',
    ],
)