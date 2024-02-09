Introduction: We are Team Thomas Malthus, with members:
    •     Brito, Steven
    •    stevenbrito@berkeley.edu (mailto:stevenbrito@berkeley.edu) stevennaa
    •    Chen, Angela
    •     akchen@berkeley.edu (mailto:akchen@berkeley.edu) angiechen17
    •    Pappas, Tia
    •    tia.pappas@berkeley.edu (mailto:tia.pappas@berkeley.edu) t-pappas
    •    Erdene-Ochir, Bolor
    •    bolorerdene@berkeley.edu (mailto:bolorerdene@berkeley.edu) bowlererdene
    •    Wang, Samantha
    •    samlwang@berkeley.edu (mailto:samlwang@berkeley.edu) samlwang2
    •    Chris Nicholas
    •    chrisgnicholas@att.net (mailto:chrisgnicholas@att.net)  chrisgnicholas
    •    Zheng, Kasper
    •    lyuheng_zheng@berkeley.edu (mailto:lyuheng_zheng@berkeley.edu)  lyvheng

Topic & Goals: 
Our project focused on comparing Namibia vs South Africa post-Namibian independence. 
Our main project goals included:
    •    How do the population growth rates and trends in each country show differences?
    •    How do rural and non-rural areas in Namibia and South Africa differ?
    •    How does land use and land quality play into the differences between the countries?
    •    How does agricultural production vary in each country?

Collaboration: We collaborated using the following tools:
    •    Github for code/repo, discussions including standup meetings, resource sharing, and idea generation,
    •    Message for communications, zoom,etc.

Code:
 Our source code can be found here: GitHub (https://github.com/Chris-Nicholas-collaborators/EEP153_team_Malthus)

Video:
 Our final presentation video can be found here: video (https://drive.google.com/file/d/16V8rwhas7EBxmoynRwFewr81r0PNvLm2/view?usp=sharing)


-----------------
Notes about branches
-----------------

Our team pushed the limits on functionality, which in turn generated challenges to merge into the main branch.
Development continued after our video was created.

Additionally, our configurations experienced considerable challenges with package management and caching of
conflicting versions of the 'wbdata' Python package, as well as numerous libraries necessary for raster
analysis under geopandas and gdal. It is possible errors will be encountered running the team notebook with the wbdata
package because of its late signature change.

As such, the main branch lags behind. Two separate branches, "feature/worldpop_example", and the "feature/animated_pyramid" branches.

Source code was structured as a Python module, and placed in the src directory, along with out Python unittest in the "test" directory.

An attempt was made to smooth installation with a Makefile. Modern software practice would utilize poetry.

