from setuptools import setup
from os import path, walk


name = 'senic_hub'


def find_data(top):
    for dirpath, _, files in walk(top):
        base = dirpath.replace(top, 'htdocs', 1)
        yield base, [path.join(dirpath, name) for name in files]


setup(
    name=name,
    version_format='{tag}.{commitcount}+{gitsha}',
    url='https://github.com/getsenic/nuimo-hub-app',
    author='Senic GmbH',
    author_email='developers@senic.com',
    license="MIT",
    description='...',
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    packages=[name],
    include_package_data=True,
    data_files=sorted(find_data('senic_hub/frontend/distribution')),
    package_dir={name: 'senic_hub'},
    package_data={
        name: [
            '.coveragerc',
            'backend/tests/*.py',
            'backend/tests/data/*.*',
            'backend/views/*.*',
        ],
    },
    zip_safe=False,
    setup_requires=[
        'setuptools-git >= 0',
        'setuptools-git-version'
    ],
    install_requires=[
        # backend
        'click',
        'colander',
        'cornice<2.0',
        'nuimo>=0.3.0,<0.4.0',
        'pyramid',
        'pyramid_tm',
        'pytz',
        'requests',
        'cryptoyaml',
        'wifi',
        'netdisco==0.9.1',
        # nuimo_app
        'websocket-client==0.40.0',
        'nuimo',
    ],
    extras_require={
        'development': [
            'tox',
        ],
    },
    entry_points="""
        [paste.app_factory]
        main = senic_hub.backend:main
        [console_scripts]
        scan_wifi = senic_hub.backend.commands:scan_wifi
        enter_wifi_setup = senic_hub.backend.commands:enter_wifi_setup
        join_wifi = senic_hub.backend.commands:join_wifi
        setup_nuimo = senic_hub.backend.commands:setup_nuimo
        create_configurations = senic_hub.backend.commands:create_configuration_files_and_restart_apps
        device_discovery = senic_hub.backend.commands:discover_devices
    """,
)