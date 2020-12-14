from distutils.core import setup

setup(
    name='delete-new-line',
    version='1.0',
    description='Delete unnecessary line breaks such as when copying pdf text.',
    author='Yuto Watanabe',
    author_email='yuto.w51942@gmail.com',
    url='https://github.com/yuto51942/delete-new-line',
    install_requires=["pyperclip"],
    packages=['delete_new_line'],
    entry_points={
        'console_scripts': [
            'dnl = delete_new_line.main:main',
        ],
    },
)
