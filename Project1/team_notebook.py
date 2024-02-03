{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Project 1 - Team Malthus\n",
    "### Introduction\n",
    "For our project, our group is focusing on ...\n",
    "### Import Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.27.0.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# %pip install cufflinks\n",
    "# %pip install wbdata\n",
    "import wbdata\n",
    "import sys\n",
    "import os\n",
    "import pandas as pd\n",
    "import datetime\n",
    "import cufflinks as cf\n",
    "import plotly.offline as py\n",
    "import plotly.graph_objs as go\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt \n",
    "\n",
    "sys.path.append('./src')\n",
    "\n",
    "from team_malthus import pop\n",
    "\n",
    "cf.go_offline()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### use function to get specific age range of data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dependency_ratios 2000: 81.5765762979549 2020: 67.11100170780416 \n"
     ]
    }
   ],
   "source": [
    "# get the scalar dependency ratio in 2000, and 2020\n",
    "# using our custom function in the 'pop' package\n",
    "children_2000 = pop.population( \n",
    "        year=2000, \n",
    "        sex=\"m\",\n",
    "        age_range=\"0-14\",\n",
    "        place=\"NAM\") \n",
    "\n",
    "working_age_2000 = pop.population( \n",
    "        year=2000, \n",
    "        sex=\"m\",\n",
    "        age_range=\"15-65\",\n",
    "        place=\"NAM\") \n",
    "\n",
    "elderly_2000 = pop.population( \n",
    "        year=2000, \n",
    "        sex=\"m\",\n",
    "        age_range=\"66-100\",\n",
    "        place=\"NAM\") \n",
    "\n",
    "children_2020 = pop.population( \n",
    "        year=2020, \n",
    "        sex=\"m\",\n",
    "        age_range=\"0-14\",\n",
    "        place=\"NAM\") \n",
    "\n",
    "working_age_2020 = pop.population( \n",
    "        year=2020, \n",
    "        sex=\"m\",\n",
    "        age_range=\"15-65\",\n",
    "        place=\"NAM\") \n",
    "\n",
    "elderly_2020 = pop.population( \n",
    "        year=2020, \n",
    "        sex=\"m\",\n",
    "        age_range=\"66-100\",\n",
    "        place=\"NAM\") \n",
    "\n",
    "dependency_ratio_2000 = ((children_2000 + elderly_2000) / working_age_2000) * 100\n",
    "dependency_ratio_2020 = ((children_2020 + elderly_2020) / working_age_2020) * 100\n",
    "\n",
    "print(f'dependency_ratios 2000: {dependency_ratio_2000} 2020: {dependency_ratio_2020} ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>male_0_4</th>\n",
       "      <th>female_0_4</th>\n",
       "      <th>male_5_9</th>\n",
       "      <th>female_5_9</th>\n",
       "      <th>male_10_14</th>\n",
       "      <th>female_10_14</th>\n",
       "      <th>male_15_19</th>\n",
       "      <th>female_15_19</th>\n",
       "      <th>male_20_24</th>\n",
       "      <th>female_20_24</th>\n",
       "      <th>...</th>\n",
       "      <th>male_60_64</th>\n",
       "      <th>female_60_64</th>\n",
       "      <th>male_65_69</th>\n",
       "      <th>female_65_69</th>\n",
       "      <th>male_70_74</th>\n",
       "      <th>female_70_74</th>\n",
       "      <th>male_75_79</th>\n",
       "      <th>female_75_79</th>\n",
       "      <th>male_80_UP</th>\n",
       "      <th>female_80_UP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>country</th>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">Namibia</th>\n",
       "      <th>2022</th>\n",
       "      <td>166945.0</td>\n",
       "      <td>166301.0</td>\n",
       "      <td>157787.0</td>\n",
       "      <td>158902.0</td>\n",
       "      <td>138796.0</td>\n",
       "      <td>141572.0</td>\n",
       "      <td>118803.0</td>\n",
       "      <td>122027.0</td>\n",
       "      <td>115272.0</td>\n",
       "      <td>118436.0</td>\n",
       "      <td>...</td>\n",
       "      <td>23387.0</td>\n",
       "      <td>32366.0</td>\n",
       "      <td>16275.0</td>\n",
       "      <td>24924.0</td>\n",
       "      <td>10542.0</td>\n",
       "      <td>17780.0</td>\n",
       "      <td>6202.0</td>\n",
       "      <td>11255.0</td>\n",
       "      <td>4109.0</td>\n",
       "      <td>10796.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021</th>\n",
       "      <td>166521.0</td>\n",
       "      <td>166054.0</td>\n",
       "      <td>155285.0</td>\n",
       "      <td>156738.0</td>\n",
       "      <td>134288.0</td>\n",
       "      <td>137180.0</td>\n",
       "      <td>117406.0</td>\n",
       "      <td>120602.0</td>\n",
       "      <td>115308.0</td>\n",
       "      <td>118434.0</td>\n",
       "      <td>...</td>\n",
       "      <td>22971.0</td>\n",
       "      <td>31661.0</td>\n",
       "      <td>16274.0</td>\n",
       "      <td>24653.0</td>\n",
       "      <td>10690.0</td>\n",
       "      <td>17456.0</td>\n",
       "      <td>6286.0</td>\n",
       "      <td>11088.0</td>\n",
       "      <td>4366.0</td>\n",
       "      <td>11105.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020</th>\n",
       "      <td>165958.0</td>\n",
       "      <td>165650.0</td>\n",
       "      <td>152328.0</td>\n",
       "      <td>154033.0</td>\n",
       "      <td>130102.0</td>\n",
       "      <td>133073.0</td>\n",
       "      <td>116947.0</td>\n",
       "      <td>120093.0</td>\n",
       "      <td>115136.0</td>\n",
       "      <td>118321.0</td>\n",
       "      <td>...</td>\n",
       "      <td>22407.0</td>\n",
       "      <td>30845.0</td>\n",
       "      <td>16089.0</td>\n",
       "      <td>24203.0</td>\n",
       "      <td>10666.0</td>\n",
       "      <td>16950.0</td>\n",
       "      <td>6193.0</td>\n",
       "      <td>10733.0</td>\n",
       "      <td>4463.0</td>\n",
       "      <td>11080.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019</th>\n",
       "      <td>165349.0</td>\n",
       "      <td>165170.0</td>\n",
       "      <td>149064.0</td>\n",
       "      <td>150923.0</td>\n",
       "      <td>126393.0</td>\n",
       "      <td>129433.0</td>\n",
       "      <td>117391.0</td>\n",
       "      <td>120493.0</td>\n",
       "      <td>115394.0</td>\n",
       "      <td>118705.0</td>\n",
       "      <td>...</td>\n",
       "      <td>21701.0</td>\n",
       "      <td>29931.0</td>\n",
       "      <td>15706.0</td>\n",
       "      <td>23580.0</td>\n",
       "      <td>10450.0</td>\n",
       "      <td>16268.0</td>\n",
       "      <td>5945.0</td>\n",
       "      <td>10229.0</td>\n",
       "      <td>4373.0</td>\n",
       "      <td>10726.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018</th>\n",
       "      <td>164604.0</td>\n",
       "      <td>164513.0</td>\n",
       "      <td>145544.0</td>\n",
       "      <td>147456.0</td>\n",
       "      <td>123276.0</td>\n",
       "      <td>126387.0</td>\n",
       "      <td>118329.0</td>\n",
       "      <td>121407.0</td>\n",
       "      <td>116388.0</td>\n",
       "      <td>119830.0</td>\n",
       "      <td>...</td>\n",
       "      <td>20982.0</td>\n",
       "      <td>29001.0</td>\n",
       "      <td>15270.0</td>\n",
       "      <td>22848.0</td>\n",
       "      <td>10188.0</td>\n",
       "      <td>15606.0</td>\n",
       "      <td>5679.0</td>\n",
       "      <td>9734.0</td>\n",
       "      <td>4249.0</td>\n",
       "      <td>10359.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">United States</th>\n",
       "      <th>1964</th>\n",
       "      <td>10238054.0</td>\n",
       "      <td>9892122.0</td>\n",
       "      <td>10229317.0</td>\n",
       "      <td>9868928.0</td>\n",
       "      <td>9361755.0</td>\n",
       "      <td>9014905.0</td>\n",
       "      <td>8052724.0</td>\n",
       "      <td>7951304.0</td>\n",
       "      <td>6268166.0</td>\n",
       "      <td>6593502.0</td>\n",
       "      <td>...</td>\n",
       "      <td>3478614.0</td>\n",
       "      <td>3889258.0</td>\n",
       "      <td>3024239.0</td>\n",
       "      <td>3645486.0</td>\n",
       "      <td>2283075.0</td>\n",
       "      <td>2859831.0</td>\n",
       "      <td>1487650.0</td>\n",
       "      <td>1961767.0</td>\n",
       "      <td>1160164.0</td>\n",
       "      <td>1842892.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1963</th>\n",
       "      <td>10326196.0</td>\n",
       "      <td>9984933.0</td>\n",
       "      <td>10102636.0</td>\n",
       "      <td>9747508.0</td>\n",
       "      <td>9027461.0</td>\n",
       "      <td>8671299.0</td>\n",
       "      <td>7805866.0</td>\n",
       "      <td>7748472.0</td>\n",
       "      <td>6007957.0</td>\n",
       "      <td>6309660.0</td>\n",
       "      <td>...</td>\n",
       "      <td>3497785.0</td>\n",
       "      <td>3895651.0</td>\n",
       "      <td>2982959.0</td>\n",
       "      <td>3556866.0</td>\n",
       "      <td>2278105.0</td>\n",
       "      <td>2803929.0</td>\n",
       "      <td>1464525.0</td>\n",
       "      <td>1901340.0</td>\n",
       "      <td>1128657.0</td>\n",
       "      <td>1769622.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1962</th>\n",
       "      <td>10374649.0</td>\n",
       "      <td>10035091.0</td>\n",
       "      <td>9913431.0</td>\n",
       "      <td>9568514.0</td>\n",
       "      <td>8888062.0</td>\n",
       "      <td>8574165.0</td>\n",
       "      <td>7456087.0</td>\n",
       "      <td>7371659.0</td>\n",
       "      <td>5699131.0</td>\n",
       "      <td>5984578.0</td>\n",
       "      <td>...</td>\n",
       "      <td>3495944.0</td>\n",
       "      <td>3881892.0</td>\n",
       "      <td>2918741.0</td>\n",
       "      <td>3433035.0</td>\n",
       "      <td>2283351.0</td>\n",
       "      <td>2762829.0</td>\n",
       "      <td>1440973.0</td>\n",
       "      <td>1843506.0</td>\n",
       "      <td>1101736.0</td>\n",
       "      <td>1705335.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1961</th>\n",
       "      <td>10370108.0</td>\n",
       "      <td>10029071.0</td>\n",
       "      <td>9880207.0</td>\n",
       "      <td>9515106.0</td>\n",
       "      <td>8627853.0</td>\n",
       "      <td>8360051.0</td>\n",
       "      <td>6940722.0</td>\n",
       "      <td>6878559.0</td>\n",
       "      <td>5575583.0</td>\n",
       "      <td>5770351.0</td>\n",
       "      <td>...</td>\n",
       "      <td>3458132.0</td>\n",
       "      <td>3834536.0</td>\n",
       "      <td>2891410.0</td>\n",
       "      <td>3349577.0</td>\n",
       "      <td>2259822.0</td>\n",
       "      <td>2691523.0</td>\n",
       "      <td>1413009.0</td>\n",
       "      <td>1783765.0</td>\n",
       "      <td>1072528.0</td>\n",
       "      <td>1640941.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1960</th>\n",
       "      <td>10294500.0</td>\n",
       "      <td>9951249.0</td>\n",
       "      <td>9698745.0</td>\n",
       "      <td>9346706.0</td>\n",
       "      <td>8334413.0</td>\n",
       "      <td>8048264.0</td>\n",
       "      <td>6582483.0</td>\n",
       "      <td>6548531.0</td>\n",
       "      <td>5480961.0</td>\n",
       "      <td>5626027.0</td>\n",
       "      <td>...</td>\n",
       "      <td>3466668.0</td>\n",
       "      <td>3833465.0</td>\n",
       "      <td>2870722.0</td>\n",
       "      <td>3280254.0</td>\n",
       "      <td>2213496.0</td>\n",
       "      <td>2600301.0</td>\n",
       "      <td>1377026.0</td>\n",
       "      <td>1718929.0</td>\n",
       "      <td>1041819.0</td>\n",
       "      <td>1574181.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>126 rows × 34 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                      male_0_4  female_0_4    male_5_9  female_5_9  \\\n",
       "country       date                                                   \n",
       "Namibia       2022    166945.0    166301.0    157787.0    158902.0   \n",
       "              2021    166521.0    166054.0    155285.0    156738.0   \n",
       "              2020    165958.0    165650.0    152328.0    154033.0   \n",
       "              2019    165349.0    165170.0    149064.0    150923.0   \n",
       "              2018    164604.0    164513.0    145544.0    147456.0   \n",
       "...                        ...         ...         ...         ...   \n",
       "United States 1964  10238054.0   9892122.0  10229317.0   9868928.0   \n",
       "              1963  10326196.0   9984933.0  10102636.0   9747508.0   \n",
       "              1962  10374649.0  10035091.0   9913431.0   9568514.0   \n",
       "              1961  10370108.0  10029071.0   9880207.0   9515106.0   \n",
       "              1960  10294500.0   9951249.0   9698745.0   9346706.0   \n",
       "\n",
       "                    male_10_14  female_10_14  male_15_19  female_15_19  \\\n",
       "country       date                                                       \n",
       "Namibia       2022    138796.0      141572.0    118803.0      122027.0   \n",
       "              2021    134288.0      137180.0    117406.0      120602.0   \n",
       "              2020    130102.0      133073.0    116947.0      120093.0   \n",
       "              2019    126393.0      129433.0    117391.0      120493.0   \n",
       "              2018    123276.0      126387.0    118329.0      121407.0   \n",
       "...                        ...           ...         ...           ...   \n",
       "United States 1964   9361755.0     9014905.0   8052724.0     7951304.0   \n",
       "              1963   9027461.0     8671299.0   7805866.0     7748472.0   \n",
       "              1962   8888062.0     8574165.0   7456087.0     7371659.0   \n",
       "              1961   8627853.0     8360051.0   6940722.0     6878559.0   \n",
       "              1960   8334413.0     8048264.0   6582483.0     6548531.0   \n",
       "\n",
       "                    male_20_24  female_20_24  ...  male_60_64  female_60_64  \\\n",
       "country       date                            ...                             \n",
       "Namibia       2022    115272.0      118436.0  ...     23387.0       32366.0   \n",
       "              2021    115308.0      118434.0  ...     22971.0       31661.0   \n",
       "              2020    115136.0      118321.0  ...     22407.0       30845.0   \n",
       "              2019    115394.0      118705.0  ...     21701.0       29931.0   \n",
       "              2018    116388.0      119830.0  ...     20982.0       29001.0   \n",
       "...                        ...           ...  ...         ...           ...   \n",
       "United States 1964   6268166.0     6593502.0  ...   3478614.0     3889258.0   \n",
       "              1963   6007957.0     6309660.0  ...   3497785.0     3895651.0   \n",
       "              1962   5699131.0     5984578.0  ...   3495944.0     3881892.0   \n",
       "              1961   5575583.0     5770351.0  ...   3458132.0     3834536.0   \n",
       "              1960   5480961.0     5626027.0  ...   3466668.0     3833465.0   \n",
       "\n",
       "                    male_65_69  female_65_69  male_70_74  female_70_74  \\\n",
       "country       date                                                       \n",
       "Namibia       2022     16275.0       24924.0     10542.0       17780.0   \n",
       "              2021     16274.0       24653.0     10690.0       17456.0   \n",
       "              2020     16089.0       24203.0     10666.0       16950.0   \n",
       "              2019     15706.0       23580.0     10450.0       16268.0   \n",
       "              2018     15270.0       22848.0     10188.0       15606.0   \n",
       "...                        ...           ...         ...           ...   \n",
       "United States 1964   3024239.0     3645486.0   2283075.0     2859831.0   \n",
       "              1963   2982959.0     3556866.0   2278105.0     2803929.0   \n",
       "              1962   2918741.0     3433035.0   2283351.0     2762829.0   \n",
       "              1961   2891410.0     3349577.0   2259822.0     2691523.0   \n",
       "              1960   2870722.0     3280254.0   2213496.0     2600301.0   \n",
       "\n",
       "                    male_75_79  female_75_79  male_80_UP  female_80_UP  \n",
       "country       date                                                      \n",
       "Namibia       2022      6202.0       11255.0      4109.0       10796.0  \n",
       "              2021      6286.0       11088.0      4366.0       11105.0  \n",
       "              2020      6193.0       10733.0      4463.0       11080.0  \n",
       "              2019      5945.0       10229.0      4373.0       10726.0  \n",
       "              2018      5679.0        9734.0      4249.0       10359.0  \n",
       "...                        ...           ...         ...           ...  \n",
       "United States 1964   1487650.0     1961767.0   1160164.0     1842892.0  \n",
       "              1963   1464525.0     1901340.0   1128657.0     1769622.0  \n",
       "              1962   1440973.0     1843506.0   1101736.0     1705335.0  \n",
       "              1961   1413009.0     1783765.0   1072528.0     1640941.0  \n",
       "              1960   1377026.0     1718929.0   1041819.0     1574181.0  \n",
       "\n",
       "[126 rows x 34 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# use our function to get a dataframe with breakdowns by age group\n",
    "\n",
    "df = pop.population_df(country=[\"USA\", \"NAM\"])\n",
    "display(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Namibia is extremely sparcely populated\n",
    "\n",
    "Below is a rendering of population density in 2020\n",
    "(source: https://hub.worldpop.org/geodata/listing?id=76 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x7f7db704d790>"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAewAAAGiCAYAAAAlePV8AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8WgzjOAAAACXBIWXMAAA9hAAAPYQGoP6dpAABxUUlEQVR4nO2deZAc1Z3nv3nU2d1V1epu9SG1LpCFAVkICTTN5fHSg2C1BhuHZ0aWGZYhzILxGDCBQeGA8cSELQ3MemzPcs7uALG2YUwEYJs1ZjQSIBgaAUIHEkII0C11t6Tuquqj7nz7h/yeXmVnnZ11/z4RL6SuzMp8LzMrv+/3e7/3ewpjjIEgCIIgiKpGrXQFCIIgCILIDQk2QRAEQdQAJNgEQRAEUQOQYBMEQRBEDUCCTRAEQRA1AAk2QRAEQdQAJNgEQRAEUQOQYBMEQRBEDUCCTRAEQRA1AAk2QRAEQdQAVS3YDz/8MObNmwe3240VK1bgnXfeqXSVCIIgCKIiVK1g/9u//Ru+973v4W//9m/x/vvvY8mSJVi5ciWGh4crXTWCIAiCKDtKtS7+sWLFClx00UX4X//rfwEADMNAb28v/uZv/gb33XdfhWtHEARBEOVFr3QFrIjH49i6dSvWrl0rPlNVFf39/RgYGLD8TiwWQywWE38bhoGRkRG0tbVBUZSS15kgCIIgAIAxhrGxMfT09EBV7XNkV6Vgnzx5EqlUCp2dnWmfd3Z24qOPPrL8zrp16/B3f/d35ageQRAEQeTk8OHDmD17tm3Hq9ox7EJZu3YtQqGQKIcOHap0lYpCVVVompZxO3kLCIIgaoOWlhZbj1eVFnZ7ezs0TcPQ0FDa50NDQ+jq6rL8jsvlgsvlKkf1SophGGmizP8vhxrouo5kMln2uhEEQRD5Y7eBVZUWttPpxLJly7Bx40bxmWEY2LhxI/r6+ipYs/JgjgOU/2aMIZVKlbtKBEEQRIWpSgsbAL73ve/hxhtvxPLly3HxxRfjpz/9KSYmJnDTTTdVumplxSqIX1EUKIoCwzAqUCOCIAiiElStYP/FX/wFTpw4gQceeACDg4O44IIL8Ic//GFKIFojYhgGVFWFrutIpVKWok4QBEHUF1U7D3u6hMNh+P3+Slej5PAANXKTEwRBVBehUAg+n8+241XlGDZxhlxBC6lUSljcBEEQRP3SEG95OyP1VFUt6dQq87HzcYAwxoRok3ATBEHUJw3xdrfT628YRknGjBVFSRPbYjoFvG5OpxO6XrXhCQRBEEQRNIRgVzty1LfcGShGtBljSCQS0DQNLS0t8Hq9dlaVIAiCqBAk2FUAF2w7SSQSiEajcDqd8Pv9eR2/FPUgCIIg7IH8plWCpmlQVTVtmpaiKEW73xVFQSqVQjAYhMPhgMvlQjQazfqdtrY2sYiK1+uFqqriuzy7WjweR3NzM9ra2vDJJ58gmUwKoU+lUtB1Pa3E43Ekk0l4PB4kk0kkEgkApzPTud1uGIYBl8sFh8OBefPmYXBwUIzJcy9BOByG2+3G5OQkHA4H2tvbMTw8jImJCUxMTIjscJOTk3A6nZg1axauvvpqdHR0YM+ePfjss89gGAZOnDgBl8uFVCoFr9eLSCSC4eFhjI2NATgdn+D3+5FMJuF2u6FpGlKpFOLxOBKJBBRFwfj4OCKRCDweDzRNQywWQ1tbG8bGxsT9UlUV4XAYhmGkzZVXFAUOhwM+nw+hUAiJRAKqqorv8HvP/w+c9phM5zkoBEVRsGjRInz66afiPhEEUT2QYFcBjDEkk0kRNKZpGhYtWoQ9e/aI7cAZAc/28lYUBbquQ1EU8dLlLnLuHudCwkWIj59PTk4iGo1CURS4XC74/X44nU6kUinMmDEDk5OTcLvdSCaTGB0dRUdHB3w+H8bGxhCNRmEYBnRdRywWQ3NzM7xeL2KxGDRNE50Fh8MhRMrhcCAajcLr9ULTNIyMjCAajWLOnDkIBoMAIIQzkUigt7dXfAacjpCPRqNiatuJEyfg8/nQ3d2N1tZW/Jf/8l/AGMP4+Diam5vR1NSEZDKJSCQCn8+HkydPQtd1tLS0wOFwIJFIiDowxkSHAoBYCY63EQA8Hg/cbjfC4TDi8bjoODQ3N4t4BEVRoGmaGPLQdR1Op1PMo+cdE03TxH11OBxpxzM/K/kIeDEizxjDkSNH0NbWhqGhIZrfTxBVBgl2BckUEc4YE5amLND8ZZ3pWLL4JhKJtBeuLGxcCPhL3TAMpFIpkZ+cW3jNzc1gjCEcDsPhcGBoaAhut1t0BrxeL0KhEJLJJAKBAADA6/XC4XBgcHAQExMTSKVSwnswOTkJ4HQudLfbDV3XMTExAbfbjZaWFoyOjsLn86GzsxOGYWB0dBSJREJYxZFIBIwxxONxuFwuJBIJ+P1+RCIRJJNJdHd3IxAIwOfzYfbs2QiHwxgZGcGJEyeE4DLGEIvFcOTIESGu4+PjmJychKZpmDt3Lo4fP45IJCIsbH4PeEcGgOi0JJNJYRXztLHxeFwIMvdA8GvLGMPJkyeRTCbh9/uRSCQwOTkp7kkqlUIsFhOdNy7q/Dzy/S6FoI6Pj8MwDLS2tmJkZMT24xNEubBah6HWocQpFcJq+pU5Zzjfz5yC1CzafKoZf8Fzy1pRFMTj8bzrxI/LBXXGjBmIRCIIBoPC2uRR6NxqdDqdiMVi8Hg8QswcDgc0TUNzczNCoRAYYzj33HPR1dWFN998E+FwWHgBJiYm4PV6hTXP3czcVc7F0OVyIZlMorm5WZw3mUzi5MmTiMVicLlcaGpqgtvtRnNzsxDfZDKJAwcOIJVKCZf0wYMHcfLkSaiqKixuHqD3jW98A4899hhCoZBwS3PrW1VVjI+PCxHXdT3N+8HvlcPhSBNofh7gdIeGezc0TRP3NpFICM+HruviGPyYZsE2Py92wocVhoaGRCeLIGoF/lucMWMGlixZgksvvRQvvfQShoaGMDQ0lLZwUqnlz+7EKWRhlxEuiIXkAecvfHl/WST439xS5pZ1sfOxuZVoGAYmJycxMjKCVColjsstPj7uzMXM4XAIdzivVzweh67rYsnTyy+/HDt37kyz3LgwcWucW6fJZFIIN3cXc1e0pmlwOByiA8E7LLIFP2PGDKiqKixl4LQQzZ07FxMTExgdHRXWumEYOHXqFCYmJvDII4/gxIkT4tjyj7ulpQVNTU2IxWLiGvHxbj4PXu4k8dSxwOkx+1gsJix5+TrL91PTNPh8PkxOTgqvh+w9kSnVFMN4PI7Dhw9jzpw5GB4exvj4uO3nIIhSwX9bo6OjCAQCWLBgAbxeL1pbW4UBInstZcxWuaqqYshubGys4us3kGCXmVxj0Fb7A2cscv7AyC5tq2PmerDMLlVZDAzDQCQSQSQSEceRRcXhcMDtdiMWiwlB5G5qeVoZD7xyOp3Ys2cPBgcHAZweg+bWKh+/5W75eDyOWCwmxI5b4IqiwO12Y3x8XATB8U6Ew+EQlv7k5KRwoUejUSSTSSHIiqLgxIkTCAaDiMViGB8fnyLKwWAwTQh5Z4kxJgLceJ2dTifi8Tj8fr8Yc5eDBnn9+DXj5+LH8/v9iMfjmJiYSBPkSCQijsPd8txFLn/Ox/bzfZ6s3Oi8brxenGQyKWICSLCJWsQwDBw8eBD/+I//KN43kUgEs2fPhtPpBHC6czo2NiY8gcDUOJEZM2ZgdHRUvJP4b7USgZkk2GVCFthC4YJszmRWbG/P5XLB5/MhGo0KUTOT7djckuRi0tXVJSLIee+WW8j8fE6nU7iZE4mECGYDzric5RSrfOza6XSKQDjuMtd1HeFwWESx67qO5uZmYb3yY/FzRiIRNDU1YWxsDJqmwe12w+v1IhqNIhaLpf1A+Q9S/nHy9vJgMC6c/J5OTk6K8WoeNBgIBBAKhWAYBjwejxgm4G0zDAMXXXQRBgcHsXfvXgDI6AI3i3WhzxC/pnI75WeRW/pmuEXR3d2NRCKBkydPFnRegqgUfMbHoUOHEIlEEI/Hxe/66NGj4vnnHd/u7m4MDg6KzrH8ezh27Fja76apqQnNzc04ceJEQR1mW9pVtjM1MNxymq47RRa06RxLTmMqi14+bnS+bzgcFlPATpw4IX4UiUQCsVgM4XBYBJwBEFY0FzQeWMWjpvmPhx/fMAyMjY0Ja1pRFESjUeFa5nXnQVLxeBxOp1PMP+dj7bxjMTExIaxI3jPmdeLn5uPPXq8XLpcrLZCMj5nzzgh3p6dSKYyPj6d9FovFRGCZHLgWjUZFLz8Wi+HVV1/Frl27RMdF0zQx1MBfJOaOCg/WA84IsLlw5M4G/z8/Jr9+fHgmUzDj5OQkPB4Pvv71rwurhCCqGafTiY6ODkxMTGBoaAiRSASJREL863a7kUgkhFExOTkpfsv89252mXNPnqIoiEQiwmDgv6dyQYJdIkp1E3lQEhfCQpBdOaOjo4hEImIbD3TKRSQSwdjYmOhZMsaEAE1MTIjP+PxrbhlGIhG4XC4hEMlkEtFoFLquiyjpiYkJJBIJhEIhAKcFbHJyEsuWLcOXvvQlpFIpMabOj8mD44DTAV3xeByTk5OizJs3Dz6fT/wI+Q9VURQx17ypqQmBQEBY+tFoVLi/uZhxT4RVpLZsmZuHMPh1CYVCiEajogcvR+Vz9z1vE58iB5zxriSTSeHF4N+V3etWQyNybINcFEVBa2sr5s+fn9PrwxjDqVOnMDQ0hKVLl5JoE9OGe6vsfkfy8Wan04lgMChiSbxer3jG4/G4GM6Szz88PGz5O+C/H+DMO5L/TmVvXLlEm1ziJcL84uTW2nThY73F1kkOCAOQZmnJrvFML3IuHvwHxx9iHiQliws/Bne983rzxCFOp1OMlfOIa6/XK1zmY2NjiMfj2Lp1K9ra2uDz+cQUrVQqJXrKvHPQ0tIi5lTruo6RkRFMTEzA4XAI1zevD29be3u7OF4wGBRz0+VgMU3TxHi+HDgoX0/ednnetfyZbP2a1zCXRZl7HOT68qGGYqLEM33H4XAgGAyK8/GOgPneK4qCcDiMF154AR0dHfjSl76E1157TQx3EEShqKoq8jcUMosl07G4x6m3t1dY1fJzL7/XDMNAOBwWs0p40Knc4baKB2KMiaBW/h4wB/+WA5rWVUaspmgViywA2Y5ZTJIN3gPONj7DE6DwCEp5DjdwWhja2tpEsBbfJluXjDG0tLQIi5pfHzkC2+l0wuVyYf78+SI4i7vGGWPweDzCgm5vbxceBC7cfHx59+7diMfjorMAQFjqbrcbkUgEg4ODwm3P283Hss3jx/KULG4183vB7w1/kcg/cN5+OauZfA/lqW2yO66YsetsyGP0LpdLXHc5wM0ckAecjpQ/66yzMDQ0hOPHj9tWH6Jx4B6tSCRS8Fx/efqqz+dDc3Mzkskkjhw5AiB71Lf5PedyuXDFFVdg3759GBoawuzZs5FIJHDkyBHLuB5+PFmo5f/LGQo5NK2rhuEvaDtEm7/AZXHNtF8m0c6UWEAW3UzIWdI8Ho8IIuNTlgzDgNvtxsyZM7Fnz5608Wke6c2Dvvh3ZHcyd/k3NzeLDGSy2La3t4Mxhrlz5worPxaLieQrY2NjYIyJQDMuTryjIAeU8Sh33mYuWvzaydHovLdtFmHzD5d3OGSLnG/jWHlKEomESPHKt5di+pZs5fOpeHIngyfI4ZH0fN+xsTEcOnQIl1xyCY4fP45du3aRtU3kDXdHNzU1IRwO5/09XdexaNEitLa2Ynh4GMFgEMlkEocOHcroceTpkXnQqplkMokPPvhAeLAOHDgAVVXR0tKC8fFxy3eq2TMm/58xhu7ubgwPDxftBc0FCbYN5LJiza6WYqPFreCCka0jkEmszW5dOWo4nweOjwlzeLAYFzweNOZyucQPYMaMGSKnuBywwcWUCz232mXRDIfDwj3NRebP/uzP8LnPfU6IxpNPPonR0VF4vd60YDDgdI+6u7sbo6OjGBoaSot058eTx6v4d+QsaeYlUOUIa/M9kIME+XWVE6rwffixzPenVPOsrZAtfB4EODk5CVVV4fF4RDAdcHrq28svv4zu7m5cddVV+Pjjj/HZZ59R/nHCEvk33tLSgo6ODhF8mQ+6rmPBggXo7u7Gq6++mte7KRAIoKmpCYODgyJehc8giUQiIo4jmUwiHA7D6XQKbx/vVFjFrMj/8mE8HqvD43H8fr+IXbEbEuwyYO6J5ZrilcnytdqPMSbEhluA8vhptu/aYelzweJWMo/W9ng8iMViiMfjIrGIPI5tGIaot5yzmwem8aAOWST4VC2n0ykSn/z0pz/FNddcg23btuFLX/oSuru705YWVVUVsVgMfr8f0WgUp06dQjweFz9anqSFR4Dza8M7HTwHOo8a59t4p8Oc5pUXvq88Pm2+r/IzIN8rHvUud/JKKdy8U8KvBx+v59HqLpcrLd0qz2h39OhRDA4OoqOjA1/4whcwOTmJYDAo3JyyW5F7TOQ25XpGidrF6tnmv4Pe3l6xTkI2+Dvl8ssvx5YtW/Dpp5/mJdaqqmLmzJnC+ubxNvJ6DQDEzBFuePChtrGxsbTfK/fCcWOEv8P5VE6n04lAIIDR0VHhASwVNIZdAfi4oXnuMcf88i7kuMCZl2OmcRjuwrXz1ptdv4FAQGQGczqdGB4eFquAcZE+duyYEPdUKoWmpiZMTEyIH874+Lj44cuZ1nhUJv9uT08PmpqaoKoqFixYgDlz5oie9EcffSQEcGRkRFjrfCqHqqqIx+NimprscZDHpZqamkSUNb9vwBkXutklzv+VrU5+3c2Wc7b7UI6fJ58OB5wegpAtA/6C4/NY+cvL3OlQFAVtbW3weDwIBoPo6emBz+fDjBkz0NTUhM8++wwulwuDg4MiBwDv7IyMjGBychITExNpQxH85cytH36frMi3k0tUltbWVvT09Ih0wZlWENR1Heeddx4++OADEWOS771tamoSwzkc/o7l00RdLpd418jH5c8mf3dyL5ws1mb4+9aqM0Fj2HUCnx4jv/yB9BeOPB6aD7LlIi8cYY5mtFus5XPzfycmJsTLn6/IxecRX3LJJdizZw/C4TCi0ahYgCMUCsHtdoulK82rVvGOjhyFzlOf8h+ZopxZZrOtrQ0XXnghksmkCJDigWt8HJ1HvHOrUR4OcLvdaVazeYEUs8tMdr1z977ZtS0HC1aLuPDxe0VREIvFRNQ4AGFp8yA/qyh5Lq7Dw8PiWR0dHU0TdgBi9TaeGx4A5s6di6VLlyIWiyGZTKKtrQ3JZBIdHR0iKOlP/uRPcOrUKXz88cfYtWsXhoaG0NLSgkAggHg8jgULFmDevHk4dOgQduzYIaYX8nopioL29nYh9rNmzRJDM8eOHcPIyEjGzi1hL16vVywMxH/PiqKI3zmHjynzFMmF4PP5kEwmpwi2YRjCNc7Pb4avNMitbwBZg28Ba6EuFWRhVwj5Ycnlus403SDXsbnoyVOEygkXXqfTKaytYDCI3t5eDA8PIxQKIRwOi4VD+Lg2HzcdHh4WQVh8/rm8uAk/dltbm+hVt7a2oqWlRUzXmjlzJr7//e9j27ZtOH78OJ599lmcPHlSzPnmaU1HRkaE9cyvF7f8+Uvf/MOVI8f5C0FeqESOuuYvIzmRijnKv1z3J1sQohwPIYuybPnyusrDG9mOK2POuiaP//MOJj83t4ScTicmJydx3XXX4Stf+Qo+++wzXHjhhWhpacHDDz+MiYkJfPrpp2htbRUJd5YtW4bt27eLFdUCgQAOHDiA5uZmMSZvGAYuvvhinDp1CkeOHMHx48dzrhlPFI8cBCZjRzIojqZpaG1txalTp6Y8i4qiiBkl4+PjlomDNE1Db28vZs+ejTfeeGPav0m7LWwS7Aoiv7yy3QaztZkPuq7D6/WiqamppFGLueAve6/XiwULFgirdXx8HGNjY8Ia4vOd+bWQ51dz8ZOnG/EXPBfWlpYWNDc3w+/3w+12i0jxWCyGefPmYfbs2fB4PHj99ddx8uRJxONxjI+P47zzzsOxY8cQDofFOBa31PlqY9xSsxIoWWD4/eTCJY+Dccz3rxIdqWzCKrchm+cn0/j7dM6da1tPTw/OPfdcfPOb38Tw8DCeeeYZHD58WAwz8NkKoVBIPDtNTU1pyWi4i5O7OXmq2qamJng8HjGPtxjx4J0MvvKcoihYsGCByAbIxzir+ZVrfl7trGtzc3Oau5mvRS8vxjFdFi5ciHg8joMHD1pulzucPO6Hd9zlhXasOhbFQC7xOiLfh1SORM7HncrFg7t2SvmC4C9AboGa4ZYYT04SCARgGKcXF/H5fCKATLa0EomEKPKLk18HOdkLFxa+YIjD4RCZxXiShOPHj6OlpUWM1fIXhtPpxIEDB8R5+TgVf9m63W5hicuJYOS2yaIlt4F7CrjI8xeEVXyCbMnKxy4F2axrebs5XWmmMXf5HkyXXG0+efIkDhw4gKeeegpvvfWWmEbIrzEP+JHvCw/eA87EEMgLncgzFjweD9rb29HR0SFWmOP51HPVze/3Y86cOaIzGQ6HMTo6iu3btyMQCCAcDmPhwoWik8rXU6+WKXGlHqaxmvWwcOFCHDx40JZzci9eKpXC4cOHM+5nHh7kyZf8fj9OnTol6litQyRkYdcg5pzQssXD3bk8mxDPMmaXFcS3y65p7laWV/eyYsaMGTj33HPhcrlEQn1d1zE0NJTmio3FYohGo2ljq7Ily13hch5wxhg6OjrgdrtFghTem49EIujo6BBj19wa0zRNLEjCGEvL1saPLccRcCEwv9zknOP8b+C0BcEziPHPzGvxZhM7u1+i/Npli86W732m4ER5HB6AmALDv5NpzM8cj2GO0TB3BOS/PR6PmLu7bNkyfPzxxwgGg6JTJA8byfXP5q7n5+dBTcCZ9JNtbW2YNWsWPB4P5s2bB4fDgd27d2N0dBQHDx4U46MulwsLFy6E0+nE4OBg2nRBHuPAz8vjVpqbm3H22WeLZ+7IkSMltbzlTk0lkZeptBM+FCYv01stkEs8T2pFsPMZ98uEPEVBnmbAX2BLly6Fpml45513bBXsYuvtcDjg8/nEfEduzQIQHRA+l5Fb5XLmM35e7sqSx594YBG3qLiI83/9fr/IWR6NRsVYMxcbPnbNOwaMMZF3mM/J5i8CbtnJ0+h4B4IHyHAXurywh3wMmUxu8ek8G1bH4tfYHCyXaX9eN+BMJ0Qe3+beDiv3uFUnxOyOtMLcWQBOi+LcuXNx6tQpnDx5EmeddRai0SiOHj0K4LSVxDtFPHBODobLRmtrq5jmJz9jfPycD6309PRg9uzZGB4eRktLC0ZHRzE5OSnOwz01Zm+JVSeEDxHNmzdPpIbdtm1bSVZ+UtXTq1Zxj1MlcblcOOecc9IWvLGDBQsWVO267STYeVJuwbbz5WoHqqriK1/5CiYnJ/Haa6/lPR7DXcH5JjUoBj72zEWMJ0vxeDxCEKLRqHCJyy8y2asgj3mbA6P4dm5JczcXt4T5AiqapmH+/PkwDEOssMXzm/Nz8nnd/KUuv/ji8TgcDgc8Hg8YY2JBE57FTfYKyB0PmWyWpV3wOpjrL2/PVS8ZPuZn3j+XZ0b+vyxsZlc8P86sWbOwePFibNq0SXhcurq6RFY7IL2zx7PWyR4R+T6ahYKvnW7lAuUdMTmBD++o8E6c+dnMNLZvvn4ul0usvDZ37lwkk0kcPXo07Xnn3plqshini9vtTku7O116enrQ0dGBHTt22HI8uyHBzpNasbDzIVcwDjDVamGMiaAOnhksn1vNBTsQCIjAsEKRl63Mdh75pSevFiYnKFEUJW3pO/5SNL/orV6OslUppzvlHQa+HQA6OzvR3NyMcDiMiYkJhMNh0QZuzcudHnn+PGOnl/L0er0Ih8NwOBxpHQ65TmYRkdtQSvg1ML/8zYvSWE0jzDbmbSaTdWk+p3kfqzHynp4epFIpnDx5Mq3e7e3taau6AWeEVx7O4PXMdm0zRS7ng9W1kj0O5m1yJ4V7x1T19PK2fr8fHo8Hn//853HBBRfggw8+wPDwMD799NOMK0k1MtwNzlfVq9YsexR01oBk+7Favej4yzCVSiEcDqO5uRlNTU1pwV1W8O/J0dKFYhbSbPWWf2Q8GhxAmgXN05Ty6V3yVCor60yuAz8ucCbSXnbt8jXADcNAKBSCrutoamoSAs0tOJ4tTXZp6rqOWCwm3LE8sYiinM7SZnY7y5aj+T5lu5Z2vaitBIR/Lv+bbzrUXPc223NgDmjjyILGk6Xs27dvSr35gi6Z2mH1mzDDhzD4fSyG1tZWkdWN11u+t7xjKAce8m3AmWmBfM6wpmkYHBzEyZMnwRjDrl27MGfOHASDwaoJTqsWAoGAWCSnkSALu47hLwZ5DDaTWJhfrLncm9nOyY9tZX0UMo7GRZbP0ebrQedzLit4qk0+Lu33+0W6Qj6W3tHRgfb2dhw4cEAk1JCnbfEXhKIoItc2Pz+PDOcR8XI9M7lH5cCuTBZZPuS6FpmOlcsaLharNssxB/K5gXSvDBfTTEsv8mdCHrOU2y8/u/KYO9/m8XjSrLJcz062+yd3wuR7mel+yJ+b68pFnketA2fSxtaTW3y68OEzO6eDlQq7LWw19y5EJchlfRX6fbN7lo9l8sLHV/O1sDLBhUcOBpPHlwuBpy4Mh8OIRCJT3F7yufKtmyyMfNiAJ10BTmc6GhkZgcPhQCAQEPPDeX3495PJ5JTP5WVDObL706ou3GuQyfrN5zngL3qn0zllyhvfnu/zNN3njmO+11ZeETmFK6epqQmLFy/O+qyYV6czDwuZAzHl55APtXCBzefZMddF9gSYx8gzeQ6sjsc70nL9ebv4c8EDMOsZvkBQPpx77rliSly1i3UpIJd4FcItPh54wl8O3ELkwUzA1N6/ORmLpmnw+/04efKk+Dwf7PgxWI05F3Nsu36Y8vQfRTkdLc3H+U+cOCGC0yKRCMbHx0X6SuB0cBm/F/K0OnkREDnxgiwavA1W49a52pZv23lHS54LztvMt0/n+FYU47KX2y0vY8oj7wFg586dGcckeYyFvI6yWTzlDoDs6ufI0wULhd93q3snP++Z7q38eyhkrL2e8Xq98Hg8YuldRVFEp1m+nz6fD3v37q37Dkw2SLCrDP4Ci0ajYqUk7rblAs4FnVt0/MXjcDjgdrunTG9wu91pf5vH20qJ2bIq5Jx21NE8l5iLBBeElpYWjI2NievNc4QriiJyVsvBadyi5+PfXCT5i4Vby2a3qbldfAqeXR0jsyDLwVSFDEMUUp9i6m7lWuZu8I6ODhw/fjzrC5kxJmILrI4rjxnzRDmZ6plP/eWZB/K9lusvHy/XtZbrac6Mx2k08R4dHcXo6KiIMTnnnHMwNjaG9vZ2nDx5Epqm4XOf+xz27dvX0GIN0Bh22ck2ligLgPw5R35R8J6+YZxZBlFRziTR58E0fHUas4gX+1LgxyvFWq8ycrRtsePpgPXLkAeN6boOj8cjLGUAYpELvg//nM/H5Z0kXj8uiNzNah56kO+ZbP3yqOZSzL3lbeSrn1XLS858PfjzzqOk+RrJdlwPRTm9sMR000uah3TM19Lcpjp9nVYU/izbnXClHFCUeI1j7p3LvfdMSTWsPpMjuLkQyKtzcevNKp/1dODBQXbChUXGrhdfprFUOT0lcGbtXV6cTidcLpcYO1dVFS0tLSLpC89Vzaej8XzViqJMWWzF3OHgqVlLCT9HpZNlyMjXgHdMVVVFT08PkskkhoeH8z5WpixswBnhtCMXtOyZsfodmdtE2I9hGDUp1qWABLtC2P3jlkUaOCPiPDjKKgq8GApd6g6w9hLIZAq4KtULkAuFHInMl/njY6k8CYfX6xX16ezsxAUXXIDXXnsNuq6L5R95NDtP2pGtreWklNcwH+RAw0wdT1VVcezYsaKm5/CVt4LBoPByZDqXHVRT54doTMgl3gBkGssrdJpVMZjFulTTiArF3IFxOBxoampKiyB2u91iHjh3kUciEbS0tGB4eFi4yFtaWsQQBHdB59u+UrhR+TW2SpRSTrJNNdM0DU1NTZicnCx6vj+PiK/WpBkEQS5xIi9kIcgU3MQXpyglVi7pasCqXoZhwOl0iih8ngCFC0ssFkM8HsexY8eEi5SPv/Lx7mg0muY+5efh6U35sqGJRAJer1fkTLe7bfL0qXJd80zzla06ij09PXC73di3b19R5+HWO4k10UiQYNcYxViomazobGI93Rd9rQXg8LF/bkUDp6PrXS4XJiYmLOd9MnZ6dbRDhw4JF7q82Adf3pSnXvX5fGLdbQAi5ardyNZnKT0o5uMX0jkLhUI4duxY0efNJyKbIOoNEuwaI18R5Mv75UMucS1mDnUtiTUAMZ4tz3HngUu5xu2tFmhIJpMIh8NpUen8HHJ8QbFku2c8gJF3Qko1DFFI0hF+Hfjyp+FwuOjzyku7EkQjYXums3Xr1uGiiy5CS0sLZs6cia985SvYu3dv2j7RaBS333472tra0NzcjK997WsYGhpK2+fQoUNYtWoVvF4vZs6ciXvuuadqFxUvJ/lEfFtlXDJn2pKPlykgSP6/HMBUSOasWoK7vHle80gkUlSQHUfOIDc5OZmWnGU6mDPI8bSqVmSLpi41vLPAS1NTE84++2x4PJ6ij8mterKuiUbEdsF+/fXXcfvtt+Ptt9/Ghg0bkEgkcNVVV6VN27nrrrvwu9/9Ds899xxef/11HDt2DNdff73YnkqlsGrVKsTjcbz11lt4+umn8dRTT+GBBx6wu7o1R6YXrzmDktkCkVdIKlUdiMxw9zkPVJvuseTo60zWZqWEWk6NyrPC+Xw+KIqCXbt2TWuKjjxnniAaDlZihoeHGQD2+uuvM8YYCwaDzOFwsOeee07ss2fPHgaADQwMMMYY+/3vf89UVWWDg4Nin0cffZT5fD4Wi8XyOm8oFGIAGqqoqsoURbHclulzvi3b9kKORSV3cTqdrLW1teL1KFdRVZW1trYyTdOmfSxd1yveHipU8i2hUMhGNWWs5It/8DVrZ8yYAQDYunUrEokE+vv7xT7nnHMO5syZg4GBAQDAwMAAFi9ejM7OTrHPypUrEQ6HsXv3bsvzxGIxhMPhtFJP5GMdZ1u4w/y5Od8y+2PAlbx+NFEaeKrFRrnGiqIgGAzaEmBXLVnbCKISlPSNYRgG7rzzTlx66aU4//zzAQCDg4NwOp0IBAJp+3Z2dmJwcFDsI4s13863WbFu3Tr4/X5Rent7bW5NZTELbj6rAsnwNZ45VmOA/GWoKAp8Ph+8Xq+lqGTqFBD5EYlE8M477zTEOKy8bOZ0aZQODkFkoqS/gNtvvx27du3Cs88+W8rTAADWrl2LUCgkyuHDh0t+zkpS6AvQ6/WipaUl5zG5iIyNjYkUm4T9ZLuu9RLQxxO32PUMMZbfcqMEUa+UTLC/853v4KWXXsKrr76K2bNni8+7uroQj8cRDAbT9h8aGkJXV5fYxxw1zv/m+5hxuVzw+XxppR7J9cLKtH18fDwtajcTTApUsssyIvIXYY/HA4/HM8WaLCYy365ofk3TxGpl+VLM+ue5kDuUBNGI2C7YjDF85zvfwQsvvIBNmzZh/vz5aduXLVsGh8OBjRs3is/27t2LQ4cOoa+vDwDQ19eHDz74IG0xgA0bNsDn8+Hcc8+1u8o1Ra6XoMPhgK5PnV6fSqXESki5jsFfjGTN2Eema24WVZ4tzUqYrFzCVvdIVVUsWrQITU1Ntq18le+zwDvOAA2dEITt2BrCxhi77bbbmN/vZ6+99ho7fvy4KJOTk2KfW2+9lc2ZM4dt2rSJvffee6yvr4/19fWJ7clkkp1//vnsqquuYtu3b2d/+MMfWEdHB1u7dm3e9WjEKHEATNM05vV6M25TVTXvYzmdzqyR51SyFzmimUfiy9cy02eFnCPT8c4991zm8/nK3ube3t6KnJcKlWosdkeJ2y7YmSr+5JNPin0ikQj79re/zVpbW5nX62Vf/epX2fHjx9OOc+DAAXbNNdcwj8fD2tvb2d13380SiUTe9ahVwZ6uOCqKwrxer+VxHA5HQVNrNE1jmqYxXddJtIu8D/K1VFW1LB2gQqfp2VV4+yp97alQqZZit2DTal1VTKH5uPn+uq5bBvsUk/WKu2EL/R5ROKXOv14tK6URRKNg92pdNE+iDsn0Qubjony5yHyPRWJdP9h1H3k2MzmrGUEQpYUW/6hiCn258v2zCSz748IQ8hKFJMbVAftjFH+p7oedx5UXSJGptVXaCKKWIAu7QWF/jASXs5tl25coH7VsrZb6WaHkKUQjQ09/AyOLdSa3Zi2LR63BrdNiRU/X9aLuVzEimO937H5+qPNINDIk2HVIPsklFEWBw+FAIpFAMpm0fBGSe7O85LrWuTpUxebZzva8KIoCXdfTBLqQ58Lu54c6kEQjQ4Jdg9jx0jKvK2xl2TkcDhLsKiPbvS+FmDHGkEwmxXPCPTGZngt5GddsnptCyJUDnyAaBQo6q1GyvTTzsYBSqVTO1KNkzZSWYqZZWd1b+bNsx+KdtGLJx2UvH9+Ozl6uDgJBNBJkYdcg/KWpKAr8fj8WLlwothUisrlegolEoug6ErkpZhaA1XecTid6e3stU9LK1KJ1yoMjCYIgC7vmUVUVY2NjYoyRr5AETH8MmjE2bauMyE4+9yfTfdR1HU6nE21tbRgaGip5B4usXIKoLCTYNQxjDKOjo2mfyWONdhy/lt3ira2tADDlGtUafM68nL1O0zS43W6oqorR0VEkEgkSVIKoc0iwa4hCxjynI7ayRVfL1nUoFKp0FWyDezr4ffV4PEilUhgfHweQuYMm38tKjwVTalSCmB40hl1DFDpHN59I3ny+V6tWthwFXytYXWseqS0Hlv3gBz/Af/tv/y1tHytKOa1KVVW4XK68n49sz12tPmMEUU7Iwq5z7LCqyCIqD5kiwBVFmdLxeP7555FMJgs6tt3PgmEYiMfjeR+T57A3DAPJZDLNa1DqZ0zTtKLnqRNEtUCrdTUQ/IVdzCpgHP69asxD3sguV3khDjntLLfMNU2DpmmIx+MVryOvn9yJaMR7RtQ/dq/WRRZ2A5HPXF0zmcS9EFdzucZO5XNwMdB1vaIiVS74oi7AmestR42nUqmsFma57pF57r+V94AgCGtoDJvIihywVAhWVrld5FMXOWiuVsZH86lnrn3yySxmHksuNgd5MfD74nA4hLVtplbuF0GUGxJsIi8KXSCilNZavukuazFLVq525TtvO1vecbOVK6cetYtMwXPAabHm+1id16qNuQIlSwF1HIhqgwSbyBvzAhCVQhacXPXggVl8KlQ1I2ewm84xMnkVStFxURQFmqZlPJdV58HpdBZ9Lm6ZZ9uHIOoVGsMm8sIcGFQtVmu2eshjtowxRCKRtO38xV9tY6j5XltZDM05vOXgwkxehmKCD837y2PnVlgdf3JysuDnJ98ANTnyfLpUyzNOEByysImsyCsuFRtZXk4KOW8h87Ttbk8ut34+LmBuTWdqAxdrt9stIrRVVYWmaXA4HGhtbbW0jrOdzw6KPQ5jDE6nM2vUrZwNjiDqDRJsIivcoqmVOaylelnbfdxcLn1d1wsS02ykUikEAgF0dnYKCzSRSCAajea9dnq2DoZ5Sc1SwKPcVVWt+qENgigVJNhEUeSyEOsx+teOtZ1lZPeu+bjxeLygxChmZJE1DAMXX3wxvva1r6W5i/NxTXPLnNc3VztKbd2Oj49jcHDQtuOZx8Pt7CgRhN2QYBOCbNHF3J0qJyfJ9nLWNG3KscrpqixV5yDXEpbFUuy1sbrO8jG5W3xwcBDHjh2D2+0uuF653My17II2exgWLVqE+fPnV6g2BJEdynRGpCEHKvEIYP63nM862/cBoL+/Hzt27MDw8HDNTa3Khnm5UbuWH9U0Dddffz0GBgZw9OhRAGfGoLNdu2xLbyaTySm5v4sJyHK5XGhtbbXVsq1WGjlbHmE/dmc6I8EmLHE6nWnWlTzdKB8BcTqdU5Z8lMc5zZHMdjHd4+UjkJqmTctdnYmenh6Mj48jEonkZdnmQm4LX6jDHCmfD7quw+12i5XBCILID7sFm1zixBT4nGWeUKOQ8Um+j5VYc5f6dCzSXAlcSr3QCV+XOhN8gYtiOHbsGMbGxpBMJtPOYY4YdzqdaGtrg8vlyngsHh3OMQyjKLFWFCVtGU+CICoHCTZhSTgcthSvfAXRar6uPAWp2CClSs+ZzpROk2+b7pKe3PNgFcjFRVvXdfj9/ikdA3P0dDECnak+BEFUHkqcQkyBi5JVUo7pMJ0XPw+uKoUruhCyWdel6kyYr9vk5CT2798/5XO32y1EmkSWIOoPsrAJgTmbFHeHc5csH7/t6ekpe27napkSJotyqSLG88FKkEdHRytQE4IgygUJNpFRqIGp+a0Nw8DIyMgUV2mx47b5YhhGWZK3yPOOM22X65TPfvVAvbWHIGoREuwGJt851bKIM8YQjUan7F/KseV8ckjbRabz8GvlcrnyGirIFWle7dRCHQmi0SDBbhA0TZuSZMMuASy1dT1dsS5EfDIljuGf22Hll2rVrFwUcp+sggYJgqgsJNgNAs/FXIpFLOqJTJHx3Jo2T1crlFJdr3zqVKwXpN7ucbHQdSAqDQl2g1GKRSwqPdUqF4W2OZc7O9c4dyZqJUe1WZhIqE5DXgai0pBgNxhyAFm9Y24nz4c+Haabna0WRLuc8QkEQeQPCXYDUozY2LF8Yrk6ClyUrSxhO8bbi8nHDZwelqjEPPJM1z2f+9EonbvpUqzXhSAKgZ6wBqXQF7EdyycW+91iRcOcdYy77+2cP63rOmbPnm3b8UpBpqh3r9eb89qSGzg/amFoiKh9SLCJimO3aGR6cfKXajKZhNvtRlNTU0HHtSKZTOLIkSPTPk454ZbgxMRE3quvEQRReUiwibKjKAp0Xa/IUoZcrHp7e/E//sf/mLKAht1uzXIJXiHn6erqyrudZGETRPVAy2sSZYdHWlfChcgX6KiW3OTlxipgrp7WKyeIaoKW1yRsoRKuTh6YU67xPjnhCYeflwu33Tgcjqp1I/M1zs1Ua32rEbpWRCUpuWCvX78eiqLgzjvvFJ9Fo1HcfvvtaGtrQ3NzM772ta9haGgo7XuHDh3CqlWr4PV6MXPmTNxzzz0NZw2VEisxKzUzZsxAd3d3Xuc1Z2XLBG9HpvZkshyTyWRJrMpUKpXXcSvx4s/0+6FgqfxhjMHpdIqAvUr8jojGpaSC/e677+Lxxx/HF77whbTP77rrLvzud7/Dc889h9dffx3Hjh3D9ddfL7anUimsWrUK8Xgcb731Fp5++mk89dRTeOCBB0pZ3Yai2KlJ02FkZATHjx+33Ca//FRVhcfjmSLGVuJstX50Pkwn3Wm28d98xa+c1z5X7nMSnMK56KKLRPwDDScQZYOViLGxMbZw4UK2YcMG9sUvfpHdcccdjDHGgsEgczgc7LnnnhP77tmzhwFgAwMDjDHGfv/73zNVVdng4KDY59FHH2U+n4/FYjHL80WjURYKhUQ5fPgwA0ClAkVRFFGstll9R9M0y+9k2r/S7at0HfKtp9PpZKqqVrwu9VZcLhfTNI2uLZWsJRQK2aqrJbOwb7/9dqxatQr9/f1pn2/duhWJRCLt83POOQdz5szBwMAAAGBgYACLFy9GZ2en2GflypUIh8PYvXu35fnWrVsHv98vSm9vbwlaRVhhttCYZL3mikbm1jJ3JTOTtWL+u5yoqjolihyobJ0KQV42lbCXeDye9/AHQdhFSQT72Wefxfvvv49169ZN2TY4OAin04lAIJD2eWdnJwYHB8U+sljz7XybFWvXrkUoFBLl8OHDNrSEyEauaVlMSlTCl6XkLm9VVae9bGapXbmGYSAWi5X9vNNBVVWR/jRT/TnV3I5agQSbKCe2C/bhw4dxxx134Je//CXcbrfdh8+Iy+WCz+dLK0Tp4NHe+eD1enH77bfD4/HkHUzGyZTyURb9clOtL2l+T+QlQDNdn2qOZq8FqvUZIOob2wV769atGB4exoUXXghd16HrOl5//XX8/Oc/h67r6OzsRDweRzAYTPve0NAQurq6AJxO7GCOGud/832I0pPthZ5vcJWiKBgbG8Njjz2GSCQilvmUp1dlOw8XbKvpWcW6JAsRqkz1K1V0cLHHzOStyDTvetasWUXXkSCIymC7YF955ZX44IMPsH37dlGWL1+ONWvWiP87HA5s3LhRfGfv3r04dOgQ+vr6AAB9fX344IMPMDw8LPbZsGEDfD4fzj33XLurTNhANgFjjGFycnKKoMjj3JlEEch/qlS+FHIsczQ9z8G9bNky20WvGLHWNE3kRje3K9sY/IEDB2g6F0HUGraGsGVAjhJnjLFbb72VzZkzh23atIm99957rK+vj/X19YntyWSSnX/++eyqq65i27dvZ3/4wx9YR0cHW7t2bd7nDIVCFY8QpJJeCo2ursZobFVV2fz589nTTz/NvvGNb+QdJVxIW/I9pqZpzOFwZD0ORTFToVK5YneUeEUEOxKJsG9/+9ustbWVeb1e9tWvfpUdP3487TsHDhxg11xzDfN4PKy9vZ3dfffdLJFI5H1OEmx7ih2imWmKVy0XTdNKcn1zXStVVVlzczPTdT3jPrquM13X6+6aU6FSa8VuwaZc4kRGFEWBpmnQNA3xeLzsgTaNMCUp0xgzgLTPHQ4HgNPDA6qqZsxaxqPEE4lEiWpMEES+UC5xomxomgav11uyNJ6Z4FHh9S7WQOY2zp49G+eddx6cTidaW1vFQiV8eVAZXdfhdDrFgiqyWHPxp4hwgqh99EpXgKhekskkxsbGpjVPupDv8v3zCYaqZ+tb0zQ0NzfD7XYjHo8jkUjkbGumffgiJ5VcIa3e4DMXnE4nIpFIpatDNBAk2ERWpiOKhYgqd7/nGxFearGebocgk6ubiyafR27l2k4mk9izZ0/aHHSruvAI8WzDFXxONmPM9rW+ZSrZgSrVymuZYH+c6x6Px8t2ToIAyCVOlJBCXqL8JchFTdM0NDU1lbB2uetTimPya2Ll2jajKAocDgecTiccDofIYAZAuMALWcGulKIm163c5GpXqebMk7eCKDck2MS0yPQiLOYFyQWNi3eh7sZqGqe1Q/B5alFuyTmdTqiqCofDAZfLJa5ToecqxXWq5qVv2TTS32ajlB4LgrCCXOLEtMj0IrTDRcpdx9ySyXXMeh3TNgwjLZiMMYaxsbGijsWtdnLnTh+ysIlyQ11EoiQ4HA5bLBA5YIosmtNMp2PCGKMpXzZRrx1EonqhNyBREhKJhG0WCGOsIhHO1eRiNzOdupHQEERtQoJNlAS7xZVHOZcqgCjTOa3gdaikoPMEKTz4jNcrX8rpseBBhARBTA8SbKIm4IFDmqZZLmhRDJqmTVmXvdA6lQuzGPNVzzJN6cq1jGm+892ng6qqYmESeclPgiCKgwSbqBm4wMRiMVuO19LSgrPPPrvg75Uq6jjXOQvZh0eP8yxolcK82hlBEMVDucSJiiJbgfk8ijy5CpE/cqR9Oa5fPWehI4hCoFziRM2QzzgpDyjjc4sdDkfWud3VHAhWrciubx5139LSIhYUASqb+IQgiPwgwSZsxSyo+VhahmEglUoJ96nD4YDb7Z5yXJ44hKZ3FQ+/H52dnWhvbxfXMh+rO5/OEreu6R4RhP1Q4hSiZBTiFuWCzf/PhZlb4DzYbHx8PO9EKnZQjy54TdOwf//+tFSwmRYOcTgcImYg17WWjyNb9VbH5/eWXOcEkT/UDSZsZbpJPXiRLW7DMNDS0oJ58+bZdq58KadY67qOyy+/vOTnSSaTaYuCZLqOPLuaHO1tBR/6yEfQ5WOTWBNEYZCFTVQ9qqpiZGQEIyMj4u96tM4Mw8CxY8cqXY00uKXM3dxW193lcom1uoEzAi53CuR/CYIoDrKwiapHTg4C5G+d1VqQmmEY+PTTT6d9HKsAMk3TpsQF5MIqHoEPUSiKgo6ODpxzzjmIxWJpi39wDwlBEPZCgk1UPdFotKgVqarZCi9lR8JKLHVdz+rWzoV8LeUkNsFgMOM15lH/HLnNtdSRIohqgVziRMmwIyismGPUwjzgctcvFosVnHAmVx2HhobEPvJcb+D0PUgkEmlBbZqmCUvcKgiNVr8iiOyQhU2UjHnz5mHZsmVlz7RV7WJtJ2ZLtZzDAE6n09Jq51H9fLoevx/Z1swmsSaI3JCFTZSMAwcOYGhoKONyjrks4UIt5VqwrO2Ez02PxWJpC6N4PB4kEglEo9GCjlXotYvFYuKcsuAyxrKKM0EQxUGCTZQMxhgmJyezbs9GoSJSjPhza7QWhZ4xJtzc8rrhY2NjRR2vGNHOZ/9s7m75+luJP0EQZyCXONEQcGGxchnXoljbjSyYMnYsJcoFmGc/4y5zflyHw5H2tzk4jbLbEcRp6FdAVCVutxsXXHDBlCld08X84q83sTZbp4UIndV0OXn+tV1149O+eFIcPofbPObN9+XbaF1totEhwSaqkng8jt27d097LNRssZkFoZ6w6tjY4V62miZmZycq3zpy8c51bpoyRtQrJNhEVWIYBmKx2LTF9dJLL8V5551nU61qj+m4kjN9167gPh4oB2T2dMj78P0URZkSnS6700mwiXqFBJsoO4WISL7JTzKNvXo8Huzbt6/gOpqPVQuuWPk68foWamGbM8rlOs90yJSxjidbydQxkFOgynWSC0HUIyTYRNnhL1weaJSLfATeauyVMYYNGzYUnDDE6tjVnGqTB2bJnYpC61upaHmre8vXRDcLsByA5na7SZiJhoMEm6gY+YqKw+FIe7EX6/KcrqvULIrVAh/bnU6nolLiJ5/X6XSK6ytnUNN1XfzLhXxiYkJ8T446J4h6huZhExUlH6Ewu06LFZdCvmc1d7ja5wdXs8WZyb1t/swwDMTjcXH9eeH7ZjqG3Fmp5utAENOBLGyi6mlvby/7PNxqF2fOdKzKUlukcgCYeXzdKqWpy+USWdKsrn++QkyWNlGvkGATVc/IyAhZTRmYznWxY2GWfM4hB+3xTGbydD2+va2tbcoxi+mo0bNC1Csk2ETVY8f0LqL8yPcsm1ubu7QPHjxouYoXQRCnoV8DUfWQi7M6ydWJ4oFiLS0taetiZzue+V7TIiIEcQYKOiOqHrKuq5tMAWVer1dE+Oc7tY7uNUFkhgSbIAiBLL78/1aBY/K2TCI7Pj5e+gpnoZZXYiMIK8glTlQV/CXLI4xpDLO8WE2fyzTuzP+t1iELeS53KaF0qES5IAubqErsXCWKaFz4c5Qr/zl/1mTx5d/JlEKVLHii3JD5QlQURVHgcrnSMlzxl+Z080LXknVerRZavlO3ijluudrMV2jjHhtZkDnys8aTtfD54HLq12XLloklXylvOVFuSvJGO3r0KL75zW+ira0NHo8HixcvxnvvvSe2M8bwwAMPoLu7Gx6PB/39/VMWaBgZGcGaNWvg8/kQCARw8803V3xMjLAfxhgSicSURBnTXRGqkm7KYlz5drz4S9HeUgmSHWJX6HU2W8tW7n++Xd5Hzrj24Ycfisj1WuoQEvWB7U/c6OgoLr30UjgcDrz88sv48MMP8T//5/9Ea2ur2OfBBx/Ez3/+czz22GPYsmULmpqasHLlSkSjUbHPmjVrsHv3bmzYsAEvvfQSNm/ejFtuucXu6hJVQCaXY7FwayhXbm2rFb7seAlnyjle6uUfcx2XL5xRL3AxzQc7rjtjDJFIRFjdzc3NUFUVTqdzWscliLxhNnPvvfeyyy67LON2wzBYV1cXe+ihh8RnwWCQuVwu9swzzzDGGPvwww8ZAPbuu++KfV5++WWmKAo7evRoXvUIhUIMAJUaLIqiMFVV897X/L3LL7+cXXbZZRWrv9PpnFJ/VVVF/RwOB1NVlem6zlwuF9N1veLXPNe1nc4+lSyqqoprX8rrpCgKc7lcTNO0ireZSvWUUChUpJJaY3t3+7e//S2WL1+Or3/965g5cyaWLl2Kf/mXfxHb9+/fj8HBQfT394vP/H4/VqxYgYGBAQDAwMAAAoEAli9fLvbp7++HqqrYsmWL5XljsRjC4XBaIWoTRVGyJtpYuHAhWlpaACBtCpLT6YRhGHjrrbfw1ltvlaWuZlRVxQ033IDbbrstzZrlXgTDMJBIJKCqKhYsWACPx5PmCbCyAivl3mcmr4dVHeTrn4tytoF7ORjLHDRmF+yPLnSroR2CsBPbBfuzzz7Do48+ioULF+KVV17Bbbfdhu9+97t4+umnAQCDg4MAgM7OzrTvdXZ2im2Dg4OYOXNm2nZd1zFjxgyxj5l169bB7/eL0tvba3fTiDLBRS0TixYtgsvlmvI5/04qlRJuy3JjGAYGBgbQ2dmJjo4O8bnZFe12u3HkyBGMj4/nXImMVUlwU7Y6VEP9ODz+gQeblYtSdwwIwnbBNgwDF154IX784x9j6dKluOWWW/Ctb30Ljz32mN2nSmPt2rUIhUKiHD58uKTnI0pLJktFURT8+7//O06ePJn2ObMYz6zUy3PPnj343//7f6d1Knh0Mu9ETExMIBKJTBlnzzbGXA2R5NNZDzzT/bBqlxzNXQgUvU3UM7YLdnd3N84999y0zz7/+c/j0KFDAICuri4AwNDQUNo+Q0NDYltXVxeGh4fTtieTSYyMjIh9zLhcLvh8vrRC1B+MMcTj8bz3r5TIHTlyBJOTk+L83PqymlKUL/L3C8WuYLNCXL6apsHlck05t/lvK3EtxFqVgwVJqIl6xnbBvvTSS7F37960zz7++GPMnTsXADB//nx0dXVh48aNYns4HMaWLVvQ19cHAOjr60MwGMTWrVvFPps2bYJhGFixYoXdVSYkvF4vLrroorwWa6hXChFFVVWndA65tZ9MJoWQyPN55XOYBcZKEM3zhYvBjrHVQqfauVwudHd359XG6eBwOKZl+RNEzWBrCBtj7J133mG6rrMf/ehHbN++feyXv/wl83q97Be/+IXYZ/369SwQCLDf/OY3bOfOney6665j8+fPZ5FIROxz9dVXs6VLl7ItW7awN998ky1cuJCtXr0673pQlHhxRdd19jd/8zcsEAhUvC52lVJGCKuqypqamkp+7mqPxq5UvfOdTUCFSiWK3VHitgs2Y4z97ne/Y+effz5zuVzsnHPOYU888UTadsMw2P333886OzuZy+ViV155Jdu7d2/aPqdOnWKrV69mzc3NzOfzsZtuuomNjY3lXQcS7OJLrYpDplLMFLFqu9bTqVuppzRlur7luJ719qxSqa9it2ArjNXnoE84HIbf7690NYgqQFVVuFwuRCKRipw/X1fydLO7VRpz/Wu9PQQxXUKhkK3xVPWT9oggMpAtgKkcQWnmc2Qab611cTPXv9bbQxDVBgk20RAkk0nLVKSVIFfKVDuo5iUfS1kvnkCHIOoREmyiIUilUtB1fYpYlMMKzCcqutg841bTtTRNQyAQSEvcUk3Ydc2t5mprmkaCTdQttB420RCwP6aOBE6/1HVdRyKRqBq3Lcuy/jf/3GqbVWcglUphdHS0JPXMF6vxbMDeDpJV25PJJK3qR9QtZGETDUdHRwdWrVoFXS9ff9Xj8eQMgsw01l6LKS+txrOztWG6Lvxqdf8ThJ2QYBN5Md0XYnNzc0ldlfkuPqEoCoaHh/HSSy8VlDFtunz+85/Hl770pbwyjlWD+Oi6npZa1eFw5FUvTdPgcDjS2sk9GtnIR9D5v1Zu8Gq4ZgRRakiwibyYroV3wQUXoLu726baTCVX/eQc04ZhIB6PlzVCfP/+/di6dauoZ6b1soHMbSnnWtbt7e3o6ekRf1sNH8jj7oqiwOPxwO12Y9GiRfje974nOmipVArJZHJa9eHnloWdn5cv9kIQ9Q6NYRNl4T//8z8BVG5urtU5y1mP8fFxOBwOcU4rgdE0LU3YVFVN20/X9bJ5BTKtiidjvn6RSAS6ruOSSy5BKpUqeTR8rQ0TEMR0ocQpRNlptIQaq1atwooVK/DrX/8au3btyrifrutoaWlBMBiEpmlYsGABPvnkE9usx3Jd90a7vwSRCbsTp5CFTZSdRnqZu91uXH311bjxxhuhKAr279+PiYkJKIoiLGp5/eZ4PA7GGJLJZMFibbbIzbA/rvZV6qxrZk+B7DYvxxx0gqhXaAybIGwg0/hyPB7H0aNHkUwmcdddd+G+++6Dy+UCYwxOpxNutzttaciJiQnx3UIt63z2z1eE893PPBafaa67YRgk1gQxTUiwCaJEcCv1iSeewC9+8Qu43W5cccUVmDlzJoDTY77RaDRNyMoZWDZdrCxmsqIJonSQS5woiI6ODjQ1NeHEiROYmJgQ03VSqVTduboLcQtrmjbFwuXfHRkZwRNPPIFAIIDt27fjyJEjadtlaiXaOVOEPU9OQxCE/dROd56oClasWIGNGzfiT//0T+H1euFyuaDrOhwOR6WrZjuFdECyCZWiKNi1axd+/OMf47HHHqubjk29tIMgagWysImCGB8fx5NPPon//M//RCwWazj3ZzHBWDzYa//+/WlBZrVMrdefIGoRmtZFFEQpckI3Cg6Ho+aDr+qhs0EQ5YLWwyYqSq4UkkRmEokEDMOA1+sty/lKkcltukFx5rSlBEHkD/1yCKJIihXEWCxmc02ssUolmi+Z9s3mHcg3T7pVWlaCIHJDgk0UzMKFCytdhaqgGE8DT5BSCezyjFiJOXeVZ+sUKIqCZDJZ00MCBFFJSLCJglAUpeJrLdcyxUbTu91um2uSnWzinikve74rbhEEURwk2ERBMMYwMjJS6WpUNbnWdlZVtWD3dKXHfu04t7xamkwmi50giHRIsImCmDdvHrnEc5DN0uSBZ263O+ca0Rxd1xGLxQoWTTtFz46ELpmuS6VXUiOIWoEEm8ibhQsX4le/+hW+9a1vVboqNY2iKJg7dy6+8Y1v5CWqmqaJ5SoVRcG5556bV+BWtYperjaTdU0Q1lDiFCJvvvCFL+C3v/0t/vVf/1V8NmPGDAAgN3kedHd3i3WmP/roI+zfvz8vUY3FYmn7HTx40BaLt9A59TQHmyAqCyVOIfJGVdUpbk1N06CqKuWQzgM+ds3HcTMJYC5htFM4My3JKZ+DW/j5fM8uqHNA1AOUOIWoGIZhTHmJplIpEus8kUVaVVW4XC7L/eRrLLuHNU2Dw+GwVch4nbLVwWpFrlKT6xyqqkLTNCiKAlVVKRkL0RCQS5wgyohhGNB1PS8L1SxahUaX50sxudFLbf3yOd1W5+HXwaoDSRD1DAk2QZQRLjL5uHzN25PJZCmrVnb4EAtg3WlQVVUE2gEQ1rQ5+UyuhC0EUS+QH4kgykyxAjNda7LaRI13Xvj1kOvHP5e9ClyoKVMa0aiQYBNEiTALpJUgFcp0RLsS7uNcSWQ4skDzsWk+T10WdnKBE40MCTZB2EQhGbucTmddBkplspTzhS8/yhiD2+3O2ytQbd4DgigF9ffGIIgKYSVWsijLwuVwOGpWZLLV204reHx8vKRTxwii1iDBJgibyDTtjQucx+MR/5+YmKiIGNnRSSiXW5oHmRWyP0HUMyTYBFFC+PrPTqcTDz30EObPnw8A8Pv9cDqdFa5ddcNd4wRBnIYEmyAkeOY2u2CMIZlMQlEUHDt2DDNnzgQAjI2NVWSaVjUKYLaxf5qyRRBnoNSkBPFHdF1Ps+p4chMu4NN1YWualnF5yTr9GeZFtvbnm+/cKm0uQVQaSk1KECXC7ILlwmqXlZcpM1c9i0wx103+TqN3ZghChgSbIP5INivPrmCtXOJTb+7ffMRWXmSEeyEK+T5weppcvV07gjBDqUmJuqFUK0gZhlG2iO5GsybNWcyKta7j8XjDXTui8SALm6gbaM5uaTFbsE6nEwsWLJj28TJZ1JmC/8yLoDidTnR2dhZdD4KoFWwX7FQqhfvvvx/z58+Hx+PBWWedhb//+7+f8qN84IEH0N3dDY/Hg/7+fuzbty/tOCMjI1izZg18Ph8CgQBuvvlmjI+P211dgig5qqrC4XCU/bz5uIgLcSObLdhEIoGhoaGizyHnETfvx//vdruh6zo8Hk/aMpp8jrau6zAMA8FgMO92EETNwmzmRz/6EWtra2MvvfQS279/P3vuuedYc3Mz+9nPfib2Wb9+PfP7/ezFF19kO3bsYNdeey2bP38+i0QiYp+rr76aLVmyhL399tvsjTfeYGeffTZbvXp13vUIhUIMABUqVKq8uFyuKZ+pqpr2t6IoWY+hquqU71ChUukSCoVs1VfbBXvVqlXsr//6r9M+u/7669maNWsYY4wZhsG6urrYQw89JLYHg0HmcrnYM888wxhj7MMPP2QA2Lvvviv2efnll5miKOzo0aN51YMEm0qpSy4RoZJf0TRtynXVNK2g60uCTaUai92CbbtL/JJLLsHGjRvx8ccfAwB27NiBN998E9dccw0AYP/+/RgcHER/f7/4jt/vx4oVKzAwMAAAGBgYQCAQwPLly8U+/f39UFUVW7ZssTxvLBZDOBxOKwSRD+Yo8HzdxKxGg5zsiqa2I3qeH4OvzMWhJTQJYiq2R4nfd999CIfDOOecc6BpGlKpFH70ox9hzZo1AIDBwUEAmBIk0tnZKbYNDg6KjFCiorqOGTNmiH3MrFu3Dn/3d39nd3OIBoCZEqXkK8T5JvWoV+xoN2MMfr8fyWQSyWQSExMT4riFHr9R7wPRONhuYf/617/GL3/5S/zqV7/C+++/j6effhr/+I//iKefftruU6Wxdu1ahEIhUQ4fPlzS8xH1R6FR5qyAzFp2zeXOF57D3CrSupqETVEU4R2LRCKW2wmCOI3tFvY999yD++67D3/5l38JAFi8eDEOHjyIdevW4cYbb0RXVxcAYGhoCN3d3eJ7Q0NDuOCCCwAAXV1dGB4eTjtuMpnEyMiI+L4Zl8sFl8tld3MIwhYURUnrEHBB5XOPzZ0Fr9eLycnJos/H/jiv2Q5KmW2MMSbmUDMpYjyTlZ2pLo3u7SAaA9st7MnJySm9ek3TxAtp/vz56OrqwsaNG8X2cDiMLVu2oK+vDwDQ19eHYDCIrVu3in02bdoEwzCwYsUKu6tMEAVTqOVnFmRZUK0seytrs1LkI4LTsYTj8XjacZqbmwuuC1niRENgawgbY+zGG29ks2bNEtO6nn/+edbe3s6+//3vi33Wr1/PAoEA+81vfsN27tzJrrvuOstpXUuXLmVbtmxhb775Jlu4cCFN66JSFcXn87Hm5mbLbRQ5XnjRdV1cO13XWVNTU8FR37quU5Q4laorVT+tKxwOszvuuIPNmTOHud1utmDBAvaDH/yAxWIxsY9hGOz+++9nnZ2dzOVysSuvvJLt3bs37TinTp1iq1evZs3Nzczn87GbbrqJjY2N5V0PEmwqpSiKojBVVWtCmKu5jnLdrOqpKIoQ8HyOR4JNpRqL3YJNy2sShM3QUo+5ySfveyFj53zYja45UU3YvbwmLf5BNATlXKaRcprnJp9rVMj9onnbRCNAi38QDUGtWl4tLS1TkooUgqqquPzyy6Fpmo21IgiiEpBgE0SeVGLaYCQSKch6NM/3NgwD7733HlmgBFEHkGATDUexU4B0XS/79KFkMlmQd8Bq7LyapogRBFE8JNhEw1Gse1xOm1kshWQ8y7UfzT0miMaCBJsgysjs2bNx1llnZdzO13gG0jsWmqZNcclXYly+2E4CdS4IYvpQlDhBlJHDhw9nFS/DMCwjqJubm9Hd3Y2PPvqolNWbgjm6vthOQqHfk69RrQYMEoTdkGATRAZKNRWsmGPyRW3KjR3t93g8SCQSSCaTBZ+3UMu8nNP3CKLckEucIEzwXPj04reHjo4OzJ07t6jvFnoP6J4R9QxZ2ARhIlNSD1oRqjgOHTpU6SoQRF1AFjZB5IBHdjdCutF8XNAUQEYQlYEEmyAyIFvUlRLqcotjPu2s904LQVQrJNgEkYFqEKZK1cG8pj1BEJWHfpUEQUzBPI5PucgJovKQYBMEAQDo7u5Gd3e35bZKr0BGFj9BUJQ4QRB/JBgMIpFIALAvYYpdVLrDQBDVAAk2QdhIrSTusKqnvEhIrbSDIBoJ8jMRRAOSS4wZY+SGJogqg36RRF1R6TnClbRKm5uboaqqLdegEeacE0StQS5xom5QFAWaphWUs7ocaJoGwzBKLoBz5sxBJBJBNBrF0NDQtMd9q1WwyV1PNCpkYRN1A2Os6sQaAFKpVFkEZs+ePTh+/Dg0TUNHR4dtx6021ziJNdGokIVNEHUCYwzxeBxDQ0O2zptmjFWdVVtt9SGIclBdXWeCIKaFYRhIJpPQNA26bk9/vBqFsRrrRBClhgSbIOoMTdPwrW99C1dccYVtx+RWdrVQTXUhiHKhsDrtqobDYfj9/kpXgygzqqo2fJINRVHgcrnAGEMsFrP92HX6yiAI2wmFQvD5fLYdj8awibrDLCqqqtbFNKV8xZIxhmg0WoYaEQRRTkiwibrCyrquF4u7Gjoc1VAHgmhUaAybIAiCIGoAEmyCIAiCqAFIsAmihKxYsSIt6ETTNMsIZ/NntRIF7fF4qi6xCkHUK/RLI4gSoSgKDh8+jPHxcfFZpqxn5s9qYaxYURScd955cLvdla4KQTQENK2LIIiiqZcIfIIoBXZP6yILmyCIoqmXCHyCqAVIsAmiwvBVxvIdt841Zlzu8W+yrgmiPJBgE0SFycetzNe5VhRlWlatw+Eo+rsEQVQWEmyCKBOZLN9UKpVThAtZTzvbfiTYBFG7kGATRJmww3Wc6xi53OHRaFRY6oVSK1PNCKJeodSkBFGjcDe5bH3nEvTpRHTTWDVBVBaysAkCtWk9MsbwxS9+EbNmzSroO/VGLd47gigGsrCJhqdWl4xkjOGtt95CMpks+Lu12mYr6qUdBJGLgi3szZs348tf/jJ6enqgKApefPHFtO2MMTzwwAPo7u6Gx+NBf38/9u3bl7bPyMgI1qxZA5/Ph0AggJtvvjktGxQA7Ny5E5dffjncbjd6e3vx4IMPFt46gsiDWn7hR6PRogSbMUaWKUHUGAUL9sTEBJYsWYKHH37YcvuDDz6In//853jsscewZcsWNDU1YeXKlWnr865Zswa7d+/Ghg0b8NJLL2Hz5s245ZZbxPZwOIyrrroKc+fOxdatW/HQQw/hhz/8IZ544okimkgQ9UGxwWKZKLSjQgJPEBWGTQMA7IUXXhB/G4bBurq62EMPPSQ+CwaDzOVysWeeeYYxxtiHH37IALB3331X7PPyyy8zRVHY0aNHGWOMPfLII6y1tZXFYjGxz7333ssWLVqUd91CoRADQIVKXRVFUSpeBypUqORXQqFQsfJqia1BZ/v378fg4CD6+/vFZ36/HytWrMDAwAAAYGBgAIFAAMuXLxf79Pf3Q1VVbNmyRexzxRVXwOl0in1WrlyJvXv3YnR01PLcsVgM4XA4rRBEvcFK5L4vJNMaQRCVwVbBHhwcBAB0dnamfd7Z2Sm2DQ4OYubMmWnbdV3HjBkz0vaxOoZ8DjPr1q2D3+8Xpbe3d/oNIogGotjOAAk9QZSHupnWtXbtWoRCIVEOHz5c6SoRRFXDhVbX9WmlOy2V1U8QRDq2CnZXVxcAYGhoKO3zoaEhsa2rqwvDw8Np25PJJEZGRtL2sTqGfA4zLpcLPp8vrRDEdGgEy1HTtIxrdJtphOtBENWMrYI9f/58dHV1YePGjeKzcDiMLVu2oK+vDwDQ19eHYDCIrVu3in02bdoEwzCwYsUKsc/mzZuRSCTEPhs2bMCiRYvQ2tpqZ5UJIiOVthxLLZCMsbzFmu9PEEQFKTRKbWxsjG3bto1t27aNAWA/+clP2LZt29jBgwcZY4ytX7+eBQIB9pvf/Ibt3LmTXXfddWz+/PksEomIY1x99dVs6dKlbMuWLezNN99kCxcuZKtXrxbbg8Eg6+zsZDfccAPbtWsXe/bZZ5nX62WPP/543vWkKHEq9VgoSpwKldopdkeJFyzYr776qmXFbrzxRsbY6ald999/P+vs7GQul4tdeeWVbO/evWnHOHXqFFu9ejVrbm5mPp+P3XTTTWxsbCxtnx07drDLLruMuVwuNmvWLLZ+/fqC6kmCTaWRSzZhV1WVhJ8KlTIUuwVbYaw+/VzhcBh+v7/S1SCIksCTqLAiFvNQVXVaQWYEQeRHKBSyNZ6qbqLECcIOaiWwijFW0BrZMlysa6WtBEGchgSbICRqyeFkh+DKxzAfjwSdIKoLEmyCqGJKKZpmd7q5s1JLnReCaARIsAmiSlDVqT/HTKLJx7DJCiaIxoEEmyCqBPbHJS8dDkdOIZ7OGDZBELWJXukKEARxxvXNGEtLGEQQBMEhC5sgqoBCp2c1NTWlrWZHEET9Q4JNEDWKpmmVrgJBEGWEXOIEUYNMTk7S+DVBNBhkYRNEDZKvWBcbRU7R5wRRfZBgE4RNVKPIcWFXFAVz5syBy+WqcI0IgigWEmyCsIlqd1G3tLTkPe5d7W0hiEaEBJsgGgDGGHbv3o3Jycmyn1tRFJx//vkU1U4Q04SCzgiihlFVNWt60WqAdxaqsW4EUUuQhU0QJaSU49qKomDJkiUIBAJThLvY45VqqhiJNUFMH7KwCaKElEqo+FrYu3fvRiqVQiqVmvYxGWNTjiNnYCsV5TgHQdQDZGETRA3CxS0ej9si1laoqgpFUeByucq6ahhBENaQhU0QNUyprFNFUWAYBgBQbnOCqBLIwiaIGoW7xYsVa0VR4PF4LK1n+ZipVAqMsbxWESMIonSQYBNEg6IoSkHu9FK53jNBnQOCSIdc4gRRo9jhBo/H43nvy13k5YLGtQkiHbKwCaLB4JZrJgEmy5YgqhMSbIIoMaUQwFKKqqZpZRVtVaXXEEHkA/1SCKLElCKCezoil6s+yWSyrO7ocrvaCaJWIcEmiBrDKsEJQRD1Dwk2QRAEQdQAJNgEQRAEUQOQYBNEHVNs8BhFihNE9UGCTRDEFGgONEFUHyTYBFFmXC4XXC5XWc6VTXhLtZQmQRClgQSbIMqIqqq48MILcfbZZ1tOzSqnK5oizQmitqDUpARRRgzDwNtvvw1N0yznH5fSFe12uxEIBDA0NEQub4KoQcjCJogywxhDMpks6Dt2WN5/9md/hv/7f/8vfD7ftI9VLij4jSDOQBY2UVEWLVqEw4cPY3JystJVqWqsLGKn01nQ4h0bNmzAJ598UtB3qgFVVSkbGkGALGyigng8HqxduxY9PT2VrgpaW1uhqmpNrflcqFs7Go1iz549iEQiJaqR/TDGSKwJ4o8orE4Hs8LhMPx+f6WrQWRBVVUEAgGMjIxUuiro7u7GiRMnAKBgd7UduFwupFKpipybIIjSEAqFbB2CIpc4UTEMw6gKsQaA48ePV/T8pbLqFUWhADOCqBNIsAmiQshiGo1GS3KORhRrGvMm6hUawyaICtGIYlosLpcr70QvdF2JeoUEmyBqHE3TaiZQrlhaW1vhdDrz2pcEm6hXyCVOEDWOYRh1L1KDg4OVrgJBVJyCLezNmzfjy1/+Mnp6eqAoCl588UWxLZFI4N5778XixYvR1NSEnp4e/NVf/RWOHTuWdoyRkRGsWbMGPp8PgUAAN998M8bHx9P22blzJy6//HK43W709vbiwQcfLK6FBFHn1KtY17vXgCAKpWDBnpiYwJIlS/Dwww9P2TY5OYn3338f999/P95//308//zz2Lt3L6699tq0/dasWYPdu3djw4YNeOmll7B582bccsstYns4HMZVV12FuXPnYuvWrXjooYfwwx/+EE888UQRTSSI2qYY4aoHsavXjghBFA2bBgDYCy+8kHWfd955hwFgBw8eZIwx9uGHHzIA7N133xX7vPzyy0xRFHb06FHGGGOPPPIIa21tZbFYTOxz7733skWLFmU8TzQaZaFQSJTDhw8zAFSoNFxRVZUpilLxelCh0uglFApNQ2GnUvKgs1AoBEVREAgEAAADAwMIBAJYvny52Ke/vx+qqmLLli1inyuuuCItyGTlypXYu3cvRkdHLc+zbt06+P1+UXp7e0vXKIKoYhphTJsgGpGSCnY0GsW9996L1atXi2wvg4ODmDlzZtp+uq5jxowZIrBkcHAQnZ2dafvwvzMFn6xduxahUEiUw4cP290cgiAIgqgYJYsSTyQS+PM//3MwxvDoo4+W6jQCl8sFl8tV8vMQBEEQRCUoiWBzsT548CA2bdqUlku1q6sLw8PDafsnk0mMjIygq6tL7DM0NJS2D/+b70MQBEEQjYTtLnEu1vv27cN//Md/oK2tLW17X18fgsEgtm7dKj7btGkTDMPAihUrxD6bN29GIpEQ+2zYsAGLFi1Ca2ur3VUmCKIE5IpUr4dIdoIoK4VGqY2NjbFt27axbdu2MQDsJz/5Cdu2bRs7ePAgi8fj7Nprr2WzZ89m27dvZ8ePHxdFjvi++uqr2dKlS9mWLVvYm2++yRYuXMhWr14ttgeDQdbZ2cluuOEGtmvXLvbss88yr9fLHn/88bzrGQqFKh4hSIUKFSpUGrfYHSVesGC/+uqrlhW78cYb2f79+zNW/NVXXxXHOHXqFFu9ejVrbm5mPp+P3XTTTWxsbCztPDt27GCXXXYZc7lcbNasWWz9+vUF1ZMEmwoVKlSoVLLYLdi0HjZBEHUBLSVKVBt2r4dNi38QBFEXkFgT9Q4JNkEQBEHUACTYBEEQBFEDkGATBEEQRA1Agk0QBEEQNQAJNkEQGaHkJgRRPZBgEwSREYq8JojqgQSbIAiCIGoAEmyCIAiCqAFIsAmCIAiiBiDBJgjCVihQjSBKAwk2QRC2QoFqBFEaSLAJgiAIogYgwSYIgiCIGoAEmyAIgiBqABJsgiAAAD6fD6pKrwSCqFbo10kQBIDT0d0U4U0Q1Yte6QoQBFEdhEKhSleBIIgskIVNEAVCVihBEJWABJsgCoTmGRMEUQlIsAmCIAiiBiDBJogqphrd7xRJThCVgX55BDENNE3D1772NTgcjpIcvxrd7z6fryo7EgRR75BgE8Q0MAwDwWAQul7/Ey64SIfDYRJsgqgAJNgEMQ0YY9i4cSMikUilq1IWdF2Hy+XC9ddfj/POO6/S1SGIhqL+zQKCIApCURRLVzxjDIZhwDAM/OEPf4BhGBWoHUE0LiTYBEGkYSXWqqqCMQbGGOLxOOLxeFWOrxNEPUMucYIgsqKqKrxeb5poVwNOpxNz5sypdDUIomyQYBMEkZNkMolUKiX+rgbRTiQSGBkZqXQ1CKJskGATBJEVwzAQjUYrXY0pMMYwPj5e6WoQRNkgwSaIBkfTNDidzkpXgyCIHFDQGUE0OKlUKs3dTRBEdUIWNkHYBCUTIQiilJBgE4RNVEMgFkEQ9QsJNkFUGWSpEwRhBQk2QVQZS5YswbJlyypdDYIgqgwKOiOIKuPDDz+kJSwJgpgCvRUIosqIx+NIJBKVrkZGNE2D2+2udDUIouEgwSaIKqTap1lVMsCOvA9Eo0IucYIgCqLS87ZplTCiUSm4q7p582Z8+ctfRk9PDxRFwYsvvphx31tvvRWKouCnP/1p2ucjIyNYs2YNfD4fAoEAbr755ikpBnfu3InLL78cbrcbvb29ePDBBwutKkEUjaZp6OnpIWuOIIiqoeC30cTEBJYsWYKHH344634vvPAC3n77bfT09EzZtmbNGuzevRsbNmzASy+9hM2bN+OWW24R28PhMK666irMnTsXW7duxUMPPYQf/vCHeOKJJwqtLkEURXt7O/70T/8UXq+30lUhCII4DZsGANgLL7ww5fMjR46wWbNmsV27drG5c+eyf/qnfxLbPvzwQwaAvfvuu+Kzl19+mSmKwo4ePcoYY+yRRx5hra2tLBaLiX3uvfdetmjRorzrFgqFGAAqVKhQoUKlIiUUChUurFmw3d9nGAZuuOEG3HPPPTjvvPOmbB8YGEAgEMDy5cvFZ/39/VBVFVu2bBH7XHHFFWkLEqxcuRJ79+7F6Oio5XljsRjC4XBaIQiCIIh6wXbB/od/+Afouo7vfve7ltsHBwcxc+bMtM90XceMGTMwODgo9uns7Ezbh//N9zGzbt06+P1+UXp7e6fbFIIgCIKoGmwV7K1bt+JnP/sZnnrqqbKnV1y7di1CoZAohw8fLuv5CaJUKIoCRVGg6zrNfyaIBsZWwX7jjTcwPDyMOXPmQNd16LqOgwcP4u6778a8efMAAF1dXRgeHk77XjKZxMjICLq6usQ+Q0NDafvwv/k+ZlwuF3w+X1ohiHqAMQbGGBwOBy644IJKV4cgiAphq2DfcMMN2LlzJ7Zv3y5KT08P7rnnHrzyyisAgL6+PgSDQWzdulV8b9OmTTAMAytWrBD7bN68OS3b04YNG7Bo0SK0trbaWWWCqBmi0SjefffdSleDIIhKUWiU2tjYGNu2bRvbtm0bA8B+8pOfsG3btrGDBw9a7m+OEmeMsauvvpotXbqUbdmyhb355pts4cKFbPXq1WJ7MBhknZ2d7IYbbmC7du1izz77LPN6vezxxx/Pu54UJU6FChUqVCpZ7I4SL1iwX331VcuK3XjjjZb7Wwn2qVOn2OrVq1lzczPz+XzspptuYmNjY2n77Nixg1122WXM5XKxWbNmsfXr1xdUTxJsKlSoUKFSyWK3YCuMVTApcAkJh8Pw+/2VrgZBEATRoIRCIVvjqSjvIkEQBEHUACTYBEEQBFED1K1g16mnnyAIgqgR7NahuhXsU6dOVboKBEEQRAMzNjZm6/Hqdj3sGTNmAAAOHTpU88Fn4XAYvb29OHz4cM0nhKmntgD11R5qS/VST+1phLYwxjA2Nma5WuV0qFvB5usY+/3+mn8oOPWUwa2e2gLUV3uoLdVLPbWn3ttSCkOxbl3iBEEQBFFPkGATBEEQRA1Qt4Ltcrnwt3/7t3C5XJWuyrShtlQv9dQeakv1Uk/tobYUT91mOiMIgiCIeqJuLWyCIAiCqCdIsAmCIAiiBiDBJgiCIIgagASbIAiCIGoAEmyCIAiCqAHqUrAffvhhzJs3D263GytWrMA777xT6SpNYd26dbjooovQ0tKCmTNn4itf+Qr27t2btk80GsXtt9+OtrY2NDc342tf+xqGhobS9jl06BBWrVoFr9eLmTNn4p577kEymSxnU6awfv16KIqCO++8U3xWa205evQovvnNb6KtrQ0ejweLFy/Ge++9J7YzxvDAAw+gu7sbHo8H/f392LdvX9oxRkZGsGbNGvh8PgQCAdx8880YHx8vaztSqRTuv/9+zJ8/Hx6PB2eddRb+/u//Pm1Rgmpty+bNm/HlL38ZPT09UBQFL774Ytp2u+q9c+dOXH755XC73ejt7cWDDz5Y9vYkEgnce++9WLx4MZqamtDT04O/+qu/wrFjx6qyPbnujcytt94KRVHw05/+tGbbsmfPHlx77bXw+/1oamrCRRddhEOHDontZXu/sTrj2WefZU6nk/3rv/4r2717N/vWt77FAoEAGxoaqnTV0li5ciV78skn2a5du9j27dvZf/2v/5XNmTOHjY+Pi31uvfVW1tvbyzZu3Mjee+899id/8ifskksuEduTySQ7//zzWX9/P9u2bRv7/e9/z9rb29natWsr0STGGGPvvPMOmzdvHvvCF77A7rjjDvF5LbVlZGSEzZ07l/33//7f2ZYtW9hnn33GXnnlFfbJJ5+IfdavX8/8fj978cUX2Y4dO9i1117L5s+fzyKRiNjn6quvZkuWLGFvv/02e+ONN9jZZ5/NVq9eXda2/OhHP2JtbW3spZdeYvv372fPPfcca25uZj/72c+qvi2///3v2Q9+8AP2/PPPMwDshRdeSNtuR71DoRDr7Oxka9asYbt27WLPPPMM83g87PHHHy9re4LBIOvv72f/9m//xj766CM2MDDALr74YrZs2bK0Y1RLe3LdG87zzz/PlixZwnp6etg//dM/1WRbPvnkEzZjxgx2zz33sPfff5998skn7De/+U2appTr/VZ3gn3xxRez22+/XfydSqVYT08PW7duXQVrlZvh4WEGgL3++uuMsdM/YIfDwZ577jmxz549exgANjAwwBg7/aCpqsoGBwfFPo8++ijz+XwsFouVtwGMsbGxMbZw4UK2YcMG9sUvflEIdq215d5772WXXXZZxu2GYbCuri720EMPic+CwSBzuVzsmWeeYYwx9uGHHzIA7N133xX7vPzyy0xRFHb06NHSVd7EqlWr2F//9V+nfXb99dezNWvWMMZqpy3mF6ld9X7kkUdYa2tr2jN27733skWLFpW1PVa88847DAA7ePAgY6x625OpLUeOHGGzZs1iu3btYnPnzk0T7Fpqy1/8xV+wb37zmxm/U873W125xOPxOLZu3Yr+/n7xmaqq6O/vx8DAQAVrlptQKATgzCpjW7duRSKRSGvLOeecgzlz5oi2DAwMYPHixejs7BT7rFy5EuFwGLt37y5j7U9z++23Y9WqVWl1BmqvLb/97W+xfPlyfP3rX8fMmTOxdOlS/Mu//IvYvn//fgwODqa1x+/3Y8WKFWntCQQCWL58udinv78fqqpiy5YtZWvLJZdcgo0bN+Ljjz8GAOzYsQNvvvkmrrnmmppri4xd9R4YGMAVV1wBp9Mp9lm5ciX27t2L0dHRMrXGmlAoBEVREAgEANRWewzDwA033IB77rkH55133pTttdIWwzDw//7f/8PnPvc5rFy5EjNnzsSKFSvS3OblfL/VlWCfPHkSqVQq7aIAQGdnJwYHBytUq9wYhoE777wTl156Kc4//3wAwODgIJxOp/ixcuS2DA4OWraVbysnzz77LN5//32sW7duyrZaa8tnn32GRx99FAsXLsQrr7yC2267Dd/97nfx9NNPp9Un23M2ODiImTNnpm3XdR0zZswoa3vuu+8+/OVf/iXOOeccOBwOLF26FHfeeSfWrFkj6snrLlONbZGxq97V9NzJRKNR3HvvvVi9erVYBaqW2vMP//AP0HUd3/3udy2310pbhoeHMT4+jvXr1+Pqq6/Gv//7v+OrX/0qrr/+erz++uuiLuV6v9Xt8pq1xO23345du3bhzTffrHRViuLw4cO44447sGHDBrjd7kpXZ9oYhoHly5fjxz/+MQBg6dKl2LVrFx577DHceOONFa5dYfz617/GL3/5S/zqV7/Ceeedh+3bt+POO+9ET09PzbWlUUgkEvjzP/9zMMbw6KOPVro6BbN161b87Gc/w/vvvw9FUSpdnWlhGAYA4LrrrsNdd90FALjgggvw1ltv4bHHHsMXv/jFstanrizs9vZ2aJo2JTpvaGgIXV1dFapVdr7zne/gpZdewquvvorZs2eLz7u6uhCPxxEMBtP2l9vS1dVl2Va+rVxs3boVw8PDuPDCC6HrOnRdx+uvv46f//zn0HUdnZ2dNdMWAOju7sa5556b9tnnP/95ERXK65PtOevq6sLw8HDa9mQyiZGRkbK255577hFW9uLFi3HDDTfgrrvuEp6QWmqLjF31rqbnDjgj1gcPHsSGDRvS1liulfa88cYbGB4expw5c8T74ODBg7j77rsxb948UZdaaEt7ezt0Xc/5PijX+62uBNvpdGLZsmXYuHGj+MwwDGzcuBF9fX0VrNlUGGP4zne+gxdeeAGbNm3C/Pnz07YvW7YMDocjrS179+7FoUOHRFv6+vrwwQcfpD34/EdufsBKyZVXXokPPvgA27dvF2X58uVYs2aN+H+ttAUALr300ilT7D7++GPMnTsXADB//nx0dXWltSccDmPLli1p7QkGg9i6davYZ9OmTTAMAytWrChDK04zOTkJVU3/mWuaJiyHWmqLjF317uvrw+bNm5FIJMQ+GzZswKJFi9Da2lqm1pyGi/W+ffvwH//xH2hra0vbXivtueGGG7Bz586090FPTw/uuecevPLKKzXVFqfTiYsuuijr+6Cs7+q8w9NqhGeffZa5XC721FNPsQ8//JDdcsstLBAIpEXnVQO33XYb8/v97LXXXmPHjx8XZXJyUuxz6623sjlz5rBNmzax9957j/X19bG+vj6xnU8VuOqqq9j27dvZH/7wB9bR0VHRaV0cOUqcsdpqyzvvvMN0XWc/+tGP2L59+9gvf/lL5vV62S9+8Quxz/r161kgEGC/+c1v2M6dO9l1111nOaVo6dKlbMuWLezNN99kCxcuLPu0rhtvvJHNmjVLTOt6/vnnWXt7O/v+979f9W0ZGxtj27ZtY9u2bWMA2E9+8hO2bds2ETVtR72DwSDr7OxkN9xwA9u1axd79tlnmdfrLcm0rmzticfj7Nprr2WzZ89m27dvT3snyFHE1dKeXPfGjDlKvJba8vzzzzOHw8GeeOIJtm/fPvbP//zPTNM09sYbb4hjlOv9VneCzRhj//zP/8zmzJnDnE4nu/jii9nbb79d6SpNAYBlefLJJ8U+kUiEffvb32atra3M6/Wyr371q+z48eNpxzlw4AC75pprmMfjYe3t7ezuu+9miUSizK2Zilmwa60tv/vd79j555/PXC4XO+ecc9gTTzyRtt0wDHb//fezzs5O5nK52JVXXsn27t2bts+pU6fY6tWrWXNzM/P5fOymm25iY2Nj5WwGC4fD7I477mBz5sxhbrebLViwgP3gBz9IE4Fqbcurr75q+Ru58cYbba33jh072GWXXcZcLhebNWsWW79+fdnbs3///ozvhFdffbXq2pPr3pixEuxaasv/+T//h5199tnM7XazJUuWsBdffDHtGOV6v9F62ARBEARRA9TVGDZBEARB1Csk2ARBEARRA5BgEwRBEEQNQIJNEARBEDUACTZBEARB1AAk2ARBEARRA5BgEwRBEEQNQIJNEARBEDUACTZBEARB1AAk2ARBEARRA5BgEwRBEEQN8P8BfDN7hUHjAdYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "f = plt.figure() \n",
    "\n",
    "src = plt.imread('data/nam_pd_2020_1km.tif')\n",
    "\n",
    "plt.imshow(src)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def get_population_df (country):\n",
    "    countries = [country]\n",
    "    indicators = {\"SP.POP.GROW\": \"population_growth\"}\n",
    "    return wbdata.get_dataframe(indicators, country=countries)   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Namibia",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          0.018870907128583525,
          0.020381999020013808,
          0.021835174914563993,
          0.02315506172558024,
          0.024360771752537147,
          0.025409840831493113,
          0.026677879262535953,
          0.027556546604634136,
          0.02830589143241724,
          0.029028197490951868,
          0.029422375663672895,
          0.02994002177198496,
          0.02991005034288996,
          0.030059415122122957,
          0.030675443304543748,
          0.028418274854226766,
          0.02655481756571021,
          0.017037752112189608,
          0.016122647464417383,
          0.019304100974618876,
          0.011612710388373415,
          0.018190950374997072,
          0.0270446507258022,
          0.027599743350487316,
          0.029061491979309295,
          0.03122569456522406,
          0.03265371637466963,
          0.03583376244841041,
          0.06422109395311004,
          0.06094360730466164,
          0.033476897123046356,
          0.03202576966054593,
          0.032408462889126355,
          0.03169138490812351,
          0.02966316369216848,
          0.027461027503379754,
          0.025829747347243526,
          0.024911507679185263,
          0.02408837584417256,
          0.02271949366692816,
          0.020275794088281174,
          0.01715589536402362,
          0.014143429021858722,
          0.012442210499651551,
          0.0120234000182311,
          0.01199835228449686,
          0.012473242341719981,
          0.013363016636182223,
          0.014303035696070054,
          0.01504735400364865,
          0.015629826656329726,
          0.0163406204857921,
          0.016944673235244068,
          0.0173094393878781,
          0.01754600380832727,
          0.01765026532755698,
          0.01756999185446695,
          0.01725164551603875,
          0.01688468173438551,
          0.017203106242391186,
          0.01635858890027464,
          0.01446359184275714
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "South Africa",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          0.027994924565017953,
          0.029786506260396806,
          0.03033439632520185,
          0.030613782432620695,
          0.0309150051024929,
          0.030922110709255435,
          0.03089295823957272,
          0.03086806671966258,
          0.030580222235670362,
          0.030138610973661883,
          0.02921523621994382,
          0.028551767940896866,
          0.02845414465699747,
          0.028085534386605104,
          0.027568289022148917,
          0.026881041867842015,
          0.02680995709209455,
          0.026971628754559163,
          0.0266104293845828,
          0.02636079666951119,
          0.025765650160927578,
          0.02579054981413975,
          0.026803679866848285,
          0.027944994483327434,
          0.029609489148857193,
          0.03278326280410937,
          0.034976763665856225,
          0.03467807046882854,
          0.03352374086770382,
          0.030783936947649693,
          0.025583962929086823,
          0.020559049545013863,
          0.018145462170323867,
          0.017310430672935695,
          0.01646039541009614,
          0.015240828018566077,
          0.013862772595189199,
          0.012445526809948149,
          0.011115545448799224,
          0.009628640255709087,
          0.008856604122041034,
          0.009101009430224849,
          0.009242093728087042,
          0.009352901688881587,
          0.009450942408175678,
          0.009635934578021477,
          0.010138772126754958,
          0.011330813387093741,
          0.011892950701330562,
          0.011930360036352283,
          0.012634056181141773,
          0.013291585245518434,
          0.013616211070758055,
          0.015762942213257247,
          0.02074016858535188,
          0.009720039820642512,
          0.0038727848785740093,
          0.012255300399431235,
          0.012950738629214698,
          0.012231792951144627,
          0.009989204185629319,
          0.008410582436777503
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "World",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          0.013417063802176443,
          0.017559873065966514,
          0.02106924398016119,
          0.020767518088060655,
          0.020571582070861183,
          0.020894027149740424,
          0.02035653939054427,
          0.02048816563476663,
          0.020800623783685523,
          0.020709672125942546,
          0.020842423149552758,
          0.019885618655219872,
          0.01968469715156118,
          0.01916982934111644,
          0.018382541564172072,
          0.017793888955999648,
          0.01740327040111822,
          0.017393521810912915,
          0.017549079646585142,
          0.01739490145795486,
          0.017531798494779594,
          0.017928451080610586,
          0.017695990400614647,
          0.017302470729795516,
          0.01735272623328754,
          0.017562038627172427,
          0.017727416399115015,
          0.017578154096550946,
          0.017292969097002953,
          0.017304761724396656,
          0.016699905990844144,
          0.01614889201313474,
          0.015681904220095078,
          0.015256164305636588,
          0.014899048420385697,
          0.014706693443915952,
          0.014431132787429135,
          0.014091194635678761,
          0.01371258579373702,
          0.01344088897463891,
          0.013261663139317648,
          0.013051037758348372,
          0.012809131756146286,
          0.012668816349421519,
          0.012558282050683545,
          0.01249805488798117,
          0.012350820635024462,
          0.012408374890195972,
          0.01230697772859557,
          0.012171673051309284,
          0.011987974113058186,
          0.0123057890217666,
          0.012235728675879187,
          0.012063275101684923,
          0.011794242412246803,
          0.011624105809708851,
          0.011419428020367661,
          0.011016741411378206,
          0.010570503032873546,
          0.0100799109272387,
          0.008670524194034357,
          0.007909645307485391
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "Similar Popualtion Growth Rates, Namibian growth rate generally higher post-independence"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Growth Rate (%)"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"c02543e9-4555-44a2-8f96-424a41c6f2a2\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"c02543e9-4555-44a2-8f96-424a41c6f2a2\")) {                    Plotly.newPlot(                        \"c02543e9-4555-44a2-8f96-424a41c6f2a2\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Namibia\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",0.018870907128583525,0.020381999020013808,0.021835174914563993,0.02315506172558024,0.024360771752537147,0.025409840831493113,0.026677879262535953,0.027556546604634136,0.02830589143241724,0.029028197490951868,0.029422375663672895,0.02994002177198496,0.02991005034288996,0.030059415122122957,0.030675443304543748,0.028418274854226766,0.02655481756571021,0.017037752112189608,0.016122647464417383,0.019304100974618876,0.011612710388373415,0.018190950374997072,0.0270446507258022,0.027599743350487316,0.029061491979309295,0.03122569456522406,0.03265371637466963,0.03583376244841041,0.06422109395311004,0.06094360730466164,0.033476897123046356,0.03202576966054593,0.032408462889126355,0.03169138490812351,0.02966316369216848,0.027461027503379754,0.025829747347243526,0.024911507679185263,0.02408837584417256,0.02271949366692816,0.020275794088281174,0.01715589536402362,0.014143429021858722,0.012442210499651551,0.0120234000182311,0.01199835228449686,0.012473242341719981,0.013363016636182223,0.014303035696070054,0.01504735400364865,0.015629826656329726,0.0163406204857921,0.016944673235244068,0.0173094393878781,0.01754600380832727,0.01765026532755698,0.01756999185446695,0.01725164551603875,0.01688468173438551,0.017203106242391186,0.01635858890027464,0.01446359184275714],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"South Africa\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",0.027994924565017953,0.029786506260396806,0.03033439632520185,0.030613782432620695,0.0309150051024929,0.030922110709255435,0.03089295823957272,0.03086806671966258,0.030580222235670362,0.030138610973661883,0.02921523621994382,0.028551767940896866,0.02845414465699747,0.028085534386605104,0.027568289022148917,0.026881041867842015,0.02680995709209455,0.026971628754559163,0.0266104293845828,0.02636079666951119,0.025765650160927578,0.02579054981413975,0.026803679866848285,0.027944994483327434,0.029609489148857193,0.03278326280410937,0.034976763665856225,0.03467807046882854,0.03352374086770382,0.030783936947649693,0.025583962929086823,0.020559049545013863,0.018145462170323867,0.017310430672935695,0.01646039541009614,0.015240828018566077,0.013862772595189199,0.012445526809948149,0.011115545448799224,0.009628640255709087,0.008856604122041034,0.009101009430224849,0.009242093728087042,0.009352901688881587,0.009450942408175678,0.009635934578021477,0.010138772126754958,0.011330813387093741,0.011892950701330562,0.011930360036352283,0.012634056181141773,0.013291585245518434,0.013616211070758055,0.015762942213257247,0.02074016858535188,0.009720039820642512,0.0038727848785740093,0.012255300399431235,0.012950738629214698,0.012231792951144627,0.009989204185629319,0.008410582436777503],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"World\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",0.013417063802176443,0.017559873065966514,0.02106924398016119,0.020767518088060655,0.020571582070861183,0.020894027149740424,0.02035653939054427,0.02048816563476663,0.020800623783685523,0.020709672125942546,0.020842423149552758,0.019885618655219872,0.01968469715156118,0.01916982934111644,0.018382541564172072,0.017793888955999648,0.01740327040111822,0.017393521810912915,0.017549079646585142,0.01739490145795486,0.017531798494779594,0.017928451080610586,0.017695990400614647,0.017302470729795516,0.01735272623328754,0.017562038627172427,0.017727416399115015,0.017578154096550946,0.017292969097002953,0.017304761724396656,0.016699905990844144,0.01614889201313474,0.015681904220095078,0.015256164305636588,0.014899048420385697,0.014706693443915952,0.014431132787429135,0.014091194635678761,0.01371258579373702,0.01344088897463891,0.013261663139317648,0.013051037758348372,0.012809131756146286,0.012668816349421519,0.012558282050683545,0.01249805488798117,0.012350820635024462,0.012408374890195972,0.01230697772859557,0.012171673051309284,0.011987974113058186,0.0123057890217666,0.012235728675879187,0.012063275101684923,0.011794242412246803,0.011624105809708851,0.011419428020367661,0.011016741411378206,0.010570503032873546,0.0100799109272387,0.008670524194034357,0.007909645307485391],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Similar Popualtion Growth Rates, Namibian growth rate generally higher post-independence\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Growth Rate (%)\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('c02543e9-4555-44a2-8f96-424a41c6f2a2');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "variable_labels = {\"SP.POP.TOTL\":\"Population\"}\n",
    "\n",
    "# Three letter codes come from wbdata.get_country()\n",
    "countries = {\"WLD\":\"World\",\n",
    "             \"NAM\":\"Namibia\",\n",
    "            \"ZAF\":\"South Africa\"}\n",
    "\n",
    "df = wbdata.get_dataframe(variable_labels, country = countries).squeeze()\n",
    "\n",
    "df = df.unstack('country')\n",
    "# Date index is of type string; change to integers\n",
    "df.index = df.index.astype(int)\n",
    "\n",
    "# Differences (over time) in logs give us growth rates\n",
    "np.log(df).diff().iplot(title=\"Similar Popualtion Growth Rates, Namibian growth rate generally higher post-independence\",\n",
    "                        yTitle=\"Growth Rate (%)\",xTitle='Year',\n",
    "                       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data from WDI on age-sex comes in the forms of variables\n",
    "# which take the form \"SP.POP.LLHH.MA\" for males\n",
    "# and \"SP.POP.LLHH.FE\" for females, where LL is the *low* end of\n",
    "# age range, like \"05\" for 5-yo, and HH is the *high* end.\n",
    "\n",
    "# We construct a list of age-ranges.\n",
    "\n",
    "# Start with an empty list of age-rages\n",
    "age_ranges = []\n",
    "\n",
    "# Ranges top out at 80, and go in five year increments\n",
    "for i in range(0,80,5):\n",
    "    age_ranges.append(f\"{i:02d}\"+f\"{i+4:02d}\")\n",
    "\n",
    "age_ranges.append(\"80UP\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "male_variables = {\"SP.POP.\"+age_range+\".MA\":\"Males \"+age_range for age_range in age_ranges}\n",
    "female_variables = {\"SP.POP.\"+age_range+\".FE\":\"Females \"+age_range for age_range in age_ranges}\n",
    "\n",
    "variables = male_variables\n",
    "variables.update(female_variables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = wbdata.get_dataframe(variables,country=\"NAM\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.27.0.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": false
       },
       "data": [
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "darkseagreen"
         },
         "name": "Men",
         "orientation": "h",
         "type": "bar",
         "x": [
          165958,
          152328,
          130102,
          116947,
          115136,
          114346,
          91394,
          70369,
          61243,
          51347,
          41557,
          31112,
          22407,
          16089,
          10666,
          6193,
          4463
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        },
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "midnightblue"
         },
         "name": "Women",
         "orientation": "h",
         "type": "bar",
         "x": [
          -165650,
          -154033,
          -133073,
          -120093,
          -118321,
          -119223,
          -96734,
          -75214,
          -65671,
          -56876,
          -49208,
          -39533,
          -30845,
          -24203,
          -16950,
          -10733,
          -11080
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        }
       ],
       "layout": {
        "barmode": "overlay",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "title": {
          "text": "Number"
         }
        },
        "yaxis": {
         "range": [
          0,
          90
         ],
         "title": {
          "text": "Age"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"46088734-cc26-41b0-a830-41cf39c664ce\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"46088734-cc26-41b0-a830-41cf39c664ce\")) {                    Plotly.newPlot(                        \"46088734-cc26-41b0-a830-41cf39c664ce\",                        [{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"darkseagreen\"},\"name\":\"Men\",\"orientation\":\"h\",\"x\":[165958.0,152328.0,130102.0,116947.0,115136.0,114346.0,91394.0,70369.0,61243.0,51347.0,41557.0,31112.0,22407.0,16089.0,10666.0,6193.0,4463.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"},{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"midnightblue\"},\"name\":\"Women\",\"orientation\":\"h\",\"x\":[-165650.0,-154033.0,-133073.0,-120093.0,-118321.0,-119223.0,-96734.0,-75214.0,-65671.0,-56876.0,-49208.0,-39533.0,-30845.0,-24203.0,-16950.0,-10733.0,-11080.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"}],                        {\"barmode\":\"overlay\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"title\":{\"text\":\"Number\"}},\"yaxis\":{\"range\":[0,90],\"title\":{\"text\":\"Age\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('46088734-cc26-41b0-a830-41cf39c664ce');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "\n",
    "py.init_notebook_mode(connected=True)\n",
    "\n",
    "layout = go.Layout(barmode='overlay',\n",
    "                   yaxis=go.layout.YAxis(range=[0, 90], title='Age'),\n",
    "                   xaxis=go.layout.XAxis(title='Number'))\n",
    "\n",
    "#year = range(2020,1960,-20)\n",
    "year=2020\n",
    "bins = [go.Bar(x = df.loc[str(year),:].filter(regex=\"Male\").values,\n",
    "               y = [int(s[:2])+1 for s in age_ranges],\n",
    "               orientation='h',\n",
    "               name='Men',\n",
    "               marker=dict(color='darkseagreen'),\n",
    "               hoverinfo='skip'\n",
    "               ),\n",
    "\n",
    "        go.Bar(x = -df.loc[str(year),:].filter(regex=\"Female\").values,\n",
    "               y=[int(s[:2])+1 for s in age_ranges],\n",
    "               orientation='h',\n",
    "               name='Women',\n",
    "               marker=dict(color = 'midnightblue'),\n",
    "               hoverinfo='skip',\n",
    "               )\n",
    "        ]\n",
    "py.iplot(dict(data=bins, layout=layout))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = wbdata.get_dataframe(variables,country=\"ZAF\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.27.0.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": false
       },
       "data": [
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "red"
         },
         "name": "Men",
         "orientation": "h",
         "type": "bar",
         "x": [
          2943869,
          2901931,
          2753974,
          2331167,
          2424376,
          2761160,
          2870783,
          2380385,
          1654462,
          1394163,
          1399527,
          971913,
          589805,
          477104,
          344200,
          203018,
          178949
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        },
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "gold"
         },
         "name": "Women",
         "orientation": "h",
         "type": "bar",
         "x": [
          -2840382,
          -2798835,
          -2660490,
          -2252086,
          -2366586,
          -2709949,
          -2819281,
          -2337648,
          -1619533,
          -1501805,
          -1698176,
          -1321598,
          -969617,
          -828009,
          -642663,
          -408430,
          -446059
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        }
       ],
       "layout": {
        "barmode": "overlay",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "title": {
          "text": "Number"
         }
        },
        "yaxis": {
         "range": [
          0,
          90
         ],
         "title": {
          "text": "Age"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"6315e874-a5e8-40a1-b346-4a5e00e11866\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"6315e874-a5e8-40a1-b346-4a5e00e11866\")) {                    Plotly.newPlot(                        \"6315e874-a5e8-40a1-b346-4a5e00e11866\",                        [{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"red\"},\"name\":\"Men\",\"orientation\":\"h\",\"x\":[2943869.0,2901931.0,2753974.0,2331167.0,2424376.0,2761160.0,2870783.0,2380385.0,1654462.0,1394163.0,1399527.0,971913.0,589805.0,477104.0,344200.0,203018.0,178949.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"},{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"gold\"},\"name\":\"Women\",\"orientation\":\"h\",\"x\":[-2840382.0,-2798835.0,-2660490.0,-2252086.0,-2366586.0,-2709949.0,-2819281.0,-2337648.0,-1619533.0,-1501805.0,-1698176.0,-1321598.0,-969617.0,-828009.0,-642663.0,-408430.0,-446059.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"}],                        {\"barmode\":\"overlay\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"title\":{\"text\":\"Number\"}},\"yaxis\":{\"range\":[0,90],\"title\":{\"text\":\"Age\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('6315e874-a5e8-40a1-b346-4a5e00e11866');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.offline as py\n",
    "import plotly.graph_objs as go\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "py.init_notebook_mode(connected=True)\n",
    "\n",
    "layout = go.Layout(barmode='overlay',\n",
    "                   yaxis=go.layout.YAxis(range=[0, 90], title='Age'),\n",
    "                   xaxis=go.layout.XAxis(title='Number'))\n",
    "\n",
    "year =2020\n",
    "\n",
    "bins = [go.Bar(x = df.loc[str(year),:].filter(regex=\"Male\").values,\n",
    "               y = [int(s[:2])+1 for s in age_ranges],\n",
    "               orientation='h',\n",
    "               name='Men',\n",
    "               marker=dict(color='red'),\n",
    "               hoverinfo='skip'\n",
    "               ),\n",
    "\n",
    "        go.Bar(x = -df.loc[str(year),:].filter(regex=\"Female\").values,\n",
    "               y=[int(s[:2])+1 for s in age_ranges],\n",
    "               orientation='h',\n",
    "               name='Women',\n",
    "               marker=dict(color = 'gold'),\n",
    "               hoverinfo='skip',\n",
    "               )\n",
    "        ]\n",
    "py.iplot(dict(data=bins, layout=layout))\n",
    "\n",
    "# fig_population_growth = go.Figure(data=[trace_population_growth], layout=layout_population_growth)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.27.0.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": false
       },
       "data": [
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "darkseagreen"
         },
         "name": "Namibia - Men",
         "orientation": "h",
         "type": "bar",
         "x": [
          165958,
          152328,
          130102,
          116947,
          115136,
          114346,
          91394,
          70369,
          61243,
          51347,
          41557,
          31112,
          22407,
          16089,
          10666,
          6193,
          4463
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        },
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "midnightblue"
         },
         "name": "Namibia - Women",
         "orientation": "h",
         "type": "bar",
         "x": [
          -165650,
          -154033,
          -133073,
          -120093,
          -118321,
          -119223,
          -96734,
          -75214,
          -65671,
          -56876,
          -49208,
          -39533,
          -30845,
          -24203,
          -16950,
          -10733,
          -11080
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        },
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "red"
         },
         "name": "South Africa - Men",
         "orientation": "h",
         "type": "bar",
         "x": [
          2943869,
          2901931,
          2753974,
          2331167,
          2424376,
          2761160,
          2870783,
          2380385,
          1654462,
          1394163,
          1399527,
          971913,
          589805,
          477104,
          344200,
          203018,
          178949
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        },
        {
         "hoverinfo": "skip",
         "marker": {
          "color": "gold"
         },
         "name": "South Africa - Women",
         "orientation": "h",
         "type": "bar",
         "x": [
          -2840382,
          -2798835,
          -2660490,
          -2252086,
          -2366586,
          -2709949,
          -2819281,
          -2337648,
          -1619533,
          -1501805,
          -1698176,
          -1321598,
          -969617,
          -828009,
          -642663,
          -408430,
          -446059
         ],
         "y": [
          1,
          6,
          11,
          16,
          21,
          26,
          31,
          36,
          41,
          46,
          51,
          56,
          61,
          66,
          71,
          76,
          81
         ]
        }
       ],
       "layout": {
        "barmode": "group",
        "legend": {
         "x": 0.75,
         "y": 1.1
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Combined Population Pyramids"
        },
        "xaxis": {
         "title": {
          "text": "Number"
         }
        },
        "yaxis": {
         "range": [
          0,
          90
         ],
         "title": {
          "text": "Age"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"67014507-9a1b-48f2-b9bd-1d711c028f5d\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"67014507-9a1b-48f2-b9bd-1d711c028f5d\")) {                    Plotly.newPlot(                        \"67014507-9a1b-48f2-b9bd-1d711c028f5d\",                        [{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"darkseagreen\"},\"name\":\"Namibia - Men\",\"orientation\":\"h\",\"x\":[165958.0,152328.0,130102.0,116947.0,115136.0,114346.0,91394.0,70369.0,61243.0,51347.0,41557.0,31112.0,22407.0,16089.0,10666.0,6193.0,4463.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"},{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"midnightblue\"},\"name\":\"Namibia - Women\",\"orientation\":\"h\",\"x\":[-165650.0,-154033.0,-133073.0,-120093.0,-118321.0,-119223.0,-96734.0,-75214.0,-65671.0,-56876.0,-49208.0,-39533.0,-30845.0,-24203.0,-16950.0,-10733.0,-11080.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"},{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"red\"},\"name\":\"South Africa - Men\",\"orientation\":\"h\",\"x\":[2943869.0,2901931.0,2753974.0,2331167.0,2424376.0,2761160.0,2870783.0,2380385.0,1654462.0,1394163.0,1399527.0,971913.0,589805.0,477104.0,344200.0,203018.0,178949.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"},{\"hoverinfo\":\"skip\",\"marker\":{\"color\":\"gold\"},\"name\":\"South Africa - Women\",\"orientation\":\"h\",\"x\":[-2840382.0,-2798835.0,-2660490.0,-2252086.0,-2366586.0,-2709949.0,-2819281.0,-2337648.0,-1619533.0,-1501805.0,-1698176.0,-1321598.0,-969617.0,-828009.0,-642663.0,-408430.0,-446059.0],\"y\":[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81],\"type\":\"bar\"}],                        {\"barmode\":\"group\",\"legend\":{\"x\":0.75,\"y\":1.1},\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"Combined Population Pyramids\"},\"xaxis\":{\"title\":{\"text\":\"Number\"}},\"yaxis\":{\"range\":[0,90],\"title\":{\"text\":\"Age\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('67014507-9a1b-48f2-b9bd-1d711c028f5d');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.offline as py\n",
    "import plotly.graph_objs as go\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "df = wbdata.get_dataframe (variables, country=\"NAM\")\n",
    "py.init_notebook_mode(connected=True)\n",
    "\n",
    "# Namibia Population Pyramid\n",
    "layout_namibia = go.Layout(barmode='overlay',\n",
    "                           yaxis=go.layout.YAxis(range=[0, 90], title='Age'),\n",
    "                           xaxis=go.layout.XAxis(title='Number'),\n",
    "                           title='Namibia Population Pyramid')\n",
    "\n",
    "year_namibia = 2020\n",
    "\n",
    "bins_NAM = [go.Bar(x = df.loc[str(year),:].filter(regex=\"Male\").values,\n",
    "                       y=[int(s[:2]) + 1 for s in age_ranges],\n",
    "                       orientation='h',\n",
    "                       name='Namibia - Men',\n",
    "                       marker=dict(color='darkseagreen'),\n",
    "                       hoverinfo='skip'),\n",
    "\n",
    "                go.Bar(x = -df.loc[str(year),:].filter(regex=\"Female\").values,\n",
    "                       y=[int(s[:2]) + 1 for s in age_ranges],\n",
    "                       orientation='h',\n",
    "                       name='Namibia - Women',\n",
    "                       marker=dict(color='midnightblue'),\n",
    "                       hoverinfo='skip',\n",
    "                       )\n",
    "                ]\n",
    "df2 = wbdata.get_dataframe (variables, country=\"ZAF\")\n",
    "\n",
    "# South Africa Population Pyramid\n",
    "layout_south_africa = go.Layout(barmode='overlay',\n",
    "                                yaxis=go.layout.YAxis(range=[0, 90], title='Age'),\n",
    "                                xaxis=go.layout.XAxis(title='Number'),\n",
    "                                title='South Africa Population Pyramid')\n",
    "\n",
    "year_south_africa = 2020\n",
    "\n",
    "bins_SSF = [go.Bar(x = df2.loc[str(year),:].filter(regex=\"Male\").values,\n",
    "                            y=[int(s[:2]) + 1 for s in age_ranges],\n",
    "                            orientation='h',\n",
    "                            name='South Africa - Men',\n",
    "                            marker=dict(color='red'),\n",
    "                            hoverinfo='skip'),\n",
    "\n",
    "                     go.Bar(x = -df2.loc[str(year),:].filter(regex=\"Female\").values,\n",
    "                            y=[int(s[:2]) + 1 for s in age_ranges],\n",
    "                            orientation='h',\n",
    "                            name='South Africa - Women',\n",
    "                            marker=dict(color='gold'),\n",
    "                            hoverinfo='skip',\n",
    "                            )\n",
    "                     ]\n",
    "\n",
    "# Combine Namibia and South Africa Population Pyramids\n",
    "fig = go.Figure(data=bins_NAM + bins_SSF, layout=go.Layout(barmode='group',\n",
    "                                                                        yaxis=go.layout.YAxis(\n",
    "                                                                            range=[0, 90], title='Age'),\n",
    "                                                                        xaxis=go.layout.XAxis(title='Number'),\n",
    "                                                                        title='Combined Population Pyramids'))\n",
    "\n",
    "# Add a legend\n",
    "fig.update_layout(legend=dict(x=0.75, y=1.1))\n",
    "\n",
    "# Show the plot\n",
    "py.iplot(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.27.0.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import wbdata\n",
    "import cufflinks as cf\n",
    "cf.go_offline()\n",
    "\n",
    "def fix_date_index(df):\n",
    "    idx_vars = df.index.names\n",
    "    new = df.reset_index()\n",
    "    new.date = new.date.astype(int)\n",
    "    return new.set_index(idx_vars)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Cereal Production & Land: Namibia and South Africa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Namibia",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          35592,
          37068,
          37208,
          39600,
          43900,
          46000,
          48200,
          51400,
          52700,
          52900,
          55100,
          56300,
          58500,
          59800,
          63000,
          63200,
          67400,
          68600,
          71000,
          73700,
          75400,
          78100,
          83800,
          87500,
          62900,
          81129,
          69239,
          83383,
          96757,
          97948,
          114785,
          31031,
          74900,
          116234,
          70885,
          89320,
          157984,
          121180,
          73899,
          120979,
          121744,
          87998,
          97334,
          127535,
          129138,
          186008.3,
          116183,
          112580,
          111738,
          118357.63,
          118338.71,
          165800,
          86599.74,
          111718.32,
          113528.8,
          74368,
          137559,
          152898,
          70800,
          174215.92,
          198771.51,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "South Africa",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          6696635,
          7089341,
          7458814,
          5838900,
          5844000,
          6183711,
          11867534,
          7003409,
          7050700,
          8137697,
          11027700,
          11950910,
          6467880,
          13579863,
          11557896,
          10273015,
          12302690,
          12755400,
          11201720,
          13377880,
          18004771,
          11762871,
          6673572,
          7927492,
          11062037,
          11691051,
          12096954,
          12140142,
          15341300,
          11558395,
          11292510.68,
          5056342.22,
          12805479.03,
          15985688.36,
          7514386.6,
          13670069.97,
          13254451.26,
          10232322.97,
          10059495.21,
          14549008.85,
          10714748.18,
          13048224.68,
          11819152.78,
          12026898.78,
          14175144.28,
          9452299.88,
          9507863.32,
          15339478.04,
          14570877.03,
          14700930.93,
          12928365.21,
          14556167.9,
          14154567.74,
          16617348.61,
          12581802.08,
          10629626.27,
          19591509.64,
          15565749.39,
          13872311.22,
          18790402.91,
          19764573.44,
          ""
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "Cereal Production in Namibia and South Africa"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Metric Tons"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"59686742-bc42-42f5-99a7-28794eca8bbc\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"59686742-bc42-42f5-99a7-28794eca8bbc\")) {                    Plotly.newPlot(                        \"59686742-bc42-42f5-99a7-28794eca8bbc\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Namibia\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",35592.0,37068.0,37208.0,39600.0,43900.0,46000.0,48200.0,51400.0,52700.0,52900.0,55100.0,56300.0,58500.0,59800.0,63000.0,63200.0,67400.0,68600.0,71000.0,73700.0,75400.0,78100.0,83800.0,87500.0,62900.0,81129.0,69239.0,83383.0,96757.0,97948.0,114785.0,31031.0,74900.0,116234.0,70885.0,89320.0,157984.0,121180.0,73899.0,120979.0,121744.0,87998.0,97334.0,127535.0,129138.0,186008.3,116183.0,112580.0,111738.0,118357.63,118338.71,165800.0,86599.74,111718.32,113528.8,74368.0,137559.0,152898.0,70800.0,174215.92,198771.51,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"South Africa\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",6696635.0,7089341.0,7458814.0,5838900.0,5844000.0,6183711.0,11867534.0,7003409.0,7050700.0,8137697.0,11027700.0,11950910.0,6467880.0,13579863.0,11557896.0,10273015.0,12302690.0,12755400.0,11201720.0,13377880.0,18004771.0,11762871.0,6673572.0,7927492.0,11062037.0,11691051.0,12096954.0,12140142.0,15341300.0,11558395.0,11292510.68,5056342.22,12805479.03,15985688.36,7514386.6,13670069.97,13254451.26,10232322.97,10059495.21,14549008.85,10714748.18,13048224.68,11819152.78,12026898.78,14175144.28,9452299.88,9507863.32,15339478.04,14570877.03,14700930.93,12928365.21,14556167.9,14154567.74,16617348.61,12581802.08,10629626.27,19591509.64,15565749.39,13872311.22,18790402.91,19764573.44,\"\"],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Cereal Production in Namibia and South Africa\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Metric Tons\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('59686742-bc42-42f5-99a7-28794eca8bbc');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "vars = {\"AG.PRD.CREL.MT\":\"Cereal production\"}\n",
    "\n",
    "use=[\"ZAF\",\"NAM\"]\n",
    "\n",
    "cereals = fix_date_index(wbdata.get_dataframe(vars,country=use)).squeeze().unstack('country')\n",
    "\n",
    "# Use this to find top producers:\n",
    "#big_producers = cereals.query('date==2020').squeeze().sort_values(ascending=False)\n",
    "#big_producers.head(20)\n",
    "\n",
    "cereals.iplot(xTitle=\"Year\",yTitle=\"Metric Tons\",\n",
    "              title=\"Cereal Production in Namibia and South Africa\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Livestock Index: Namibia and the World"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "China",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          3.33,
          3.74,
          5.02,
          6.05,
          6.74,
          7.23,
          7.54,
          7.53,
          7.48,
          7.51,
          8.42,
          9.17,
          9.34,
          9.43,
          9.77,
          9.75,
          9.9,
          10.68,
          12.49,
          13.97,
          14.55,
          15.54,
          16.19,
          18.62,
          20.4,
          21.61,
          23.7,
          26.48,
          28,
          30.27,
          33.75,
          37.06,
          41.56,
          47.28,
          54.54,
          53.5,
          58.36,
          63.25,
          66.8,
          68.08,
          69.41,
          71.34,
          74.54,
          77.28,
          81.31,
          83.26,
          82.84,
          87.11,
          90.25,
          92.48,
          92.85,
          96.45,
          97.34,
          99.17,
          100.66,
          100.17,
          99.99,
          100.49,
          96.97,
          98.27,
          108.02,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "India",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          14.53,
          14.62,
          14.67,
          14.64,
          14.69,
          14.87,
          15.13,
          15.81,
          16.09,
          15.96,
          16.83,
          17.05,
          17.42,
          18.16,
          18.87,
          19.84,
          20.58,
          21.01,
          21.9,
          22.81,
          24.22,
          25.68,
          27.25,
          28.6,
          30.06,
          31.15,
          31.99,
          32.9,
          34.46,
          35.65,
          37.84,
          38.7,
          38.44,
          40.05,
          42.36,
          43.02,
          44.99,
          47.56,
          49.88,
          51.39,
          53.74,
          55.4,
          57.08,
          60.23,
          62.68,
          66.08,
          69.98,
          72.8,
          76.03,
          79.5,
          83.28,
          86.44,
          90.34,
          95.33,
          99.83,
          104.84,
          110.49,
          116.58,
          122.6,
          125.44,
          125.18,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Namibia",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          128.18,
          109.17,
          139.11,
          139.14,
          136.38,
          127.33,
          148.73,
          157,
          154.15,
          167.88,
          183.6,
          204.93,
          213.48,
          218.97,
          139.67,
          155.83,
          147.09,
          161.68,
          168.47,
          179.91,
          183.69,
          136.85,
          112.78,
          116.69,
          129.34,
          134.77,
          146.85,
          146.46,
          159.44,
          149.74,
          100.01,
          95.87,
          96.67,
          97.75,
          92.4,
          91,
          72.94,
          80.76,
          105.48,
          131.85,
          112.18,
          110.28,
          115.66,
          102.81,
          101.69,
          99.36,
          101.29,
          103.04,
          103.9,
          104.38,
          104.63,
          106.32,
          105.93,
          103.37,
          97.78,
          98.85,
          102.95,
          97.29,
          96.69,
          96.86,
          98.07,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(128, 0, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Russian Federation",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          125.9,
          119.69,
          109.49,
          97.2,
          89.8,
          83.87,
          81.06,
          75.51,
          76.47,
          77.28,
          79.97,
          81.34,
          79.86,
          77.82,
          79.21,
          81.91,
          85.33,
          87.73,
          89.46,
          90.44,
          93.83,
          94.84,
          98.34,
          100.58,
          101.07,
          103.94,
          106.06,
          107.98,
          110.94,
          111.81,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(219, 64, 82, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "United States",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          51.35,
          51.44,
          53.22,
          56.31,
          55.51,
          56.74,
          58.26,
          58.75,
          59.08,
          60.41,
          61.71,
          61.97,
          59.12,
          62.33,
          62.22,
          66.24,
          65.99,
          65,
          63.6,
          65.4,
          66.81,
          66.47,
          68.52,
          68.49,
          70.03,
          71.1,
          71.24,
          72.72,
          72.62,
          73.1,
          73.26,
          75.22,
          75.59,
          77.75,
          79.65,
          81.7,
          82.96,
          84.27,
          86.8,
          88.49,
          89.11,
          89.46,
          91.4,
          91.39,
          90.6,
          91.47,
          94.39,
          96.98,
          96.14,
          96.27,
          97.75,
          98.43,
          98.78,
          98.95,
          98.65,
          102.4,
          105.17,
          107.78,
          109.31,
          110.86,
          112.09,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(0, 128, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "World",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          ""
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "Livestock Index (1960-2020)"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Metric Tons"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"37e53693-8701-4454-9948-8b6a47aed260\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"37e53693-8701-4454-9948-8b6a47aed260\")) {                    Plotly.newPlot(                        \"37e53693-8701-4454-9948-8b6a47aed260\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"China\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",3.33,3.74,5.02,6.05,6.74,7.23,7.54,7.53,7.48,7.51,8.42,9.17,9.34,9.43,9.77,9.75,9.9,10.68,12.49,13.97,14.55,15.54,16.19,18.62,20.4,21.61,23.7,26.48,28.0,30.27,33.75,37.06,41.56,47.28,54.54,53.5,58.36,63.25,66.8,68.08,69.41,71.34,74.54,77.28,81.31,83.26,82.84,87.11,90.25,92.48,92.85,96.45,97.34,99.17,100.66,100.17,99.99,100.49,96.97,98.27,108.02,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"India\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",14.53,14.62,14.67,14.64,14.69,14.87,15.13,15.81,16.09,15.96,16.83,17.05,17.42,18.16,18.87,19.84,20.58,21.01,21.9,22.81,24.22,25.68,27.25,28.6,30.06,31.15,31.99,32.9,34.46,35.65,37.84,38.7,38.44,40.05,42.36,43.02,44.99,47.56,49.88,51.39,53.74,55.4,57.08,60.23,62.68,66.08,69.98,72.8,76.03,79.5,83.28,86.44,90.34,95.33,99.83,104.84,110.49,116.58,122.6,125.44,125.18,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Namibia\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",128.18,109.17,139.11,139.14,136.38,127.33,148.73,157.0,154.15,167.88,183.6,204.93,213.48,218.97,139.67,155.83,147.09,161.68,168.47,179.91,183.69,136.85,112.78,116.69,129.34,134.77,146.85,146.46,159.44,149.74,100.01,95.87,96.67,97.75,92.4,91.0,72.94,80.76,105.48,131.85,112.18,110.28,115.66,102.81,101.69,99.36,101.29,103.04,103.9,104.38,104.63,106.32,105.93,103.37,97.78,98.85,102.95,97.29,96.69,96.86,98.07,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(128, 0, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Russian Federation\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",125.9,119.69,109.49,97.2,89.8,83.87,81.06,75.51,76.47,77.28,79.97,81.34,79.86,77.82,79.21,81.91,85.33,87.73,89.46,90.44,93.83,94.84,98.34,100.58,101.07,103.94,106.06,107.98,110.94,111.81,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(219, 64, 82, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"United States\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",51.35,51.44,53.22,56.31,55.51,56.74,58.26,58.75,59.08,60.41,61.71,61.97,59.12,62.33,62.22,66.24,65.99,65.0,63.6,65.4,66.81,66.47,68.52,68.49,70.03,71.1,71.24,72.72,72.62,73.1,73.26,75.22,75.59,77.75,79.65,81.7,82.96,84.27,86.8,88.49,89.11,89.46,91.4,91.39,90.6,91.47,94.39,96.98,96.14,96.27,97.75,98.43,98.78,98.95,98.65,102.4,105.17,107.78,109.31,110.86,112.09,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(0, 128, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"World\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Livestock Index (1960-2020)\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Metric Tons\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('37e53693-8701-4454-9948-8b6a47aed260');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "elem = {\"AG.PRD.LVSK.XD\":\"Livestock index\"}\n",
    "\n",
    "uses=[\"NAM\",\"USA\",\"IND\",\"CHN\",\"RUS\",\"WLD\"]\n",
    "\n",
    "geo = (fix_date_index(wbdata.get_dataframe(elem,country=uses)).squeeze().unstack('country'))\n",
    "geo.iplot(xTitle=\"Year\",yTitle=\"Metric Tons\", title=\"Livestock Index (1960-2020)\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Crop Index: Namibia and the World"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "China",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          14.28,
          15.01,
          15.45,
          16.24,
          17.7,
          19.1,
          19.26,
          19.15,
          19.41,
          20.79,
          21.32,
          20.62,
          23.41,
          23.31,
          23.79,
          23.41,
          23.99,
          26.45,
          26.88,
          26.6,
          27.81,
          30.44,
          32.83,
          35.38,
          34.15,
          34.85,
          36.72,
          36.73,
          37.51,
          40.21,
          41.45,
          42.83,
          45.64,
          46.5,
          49.73,
          53.59,
          54.9,
          56.59,
          58.59,
          62.15,
          63.47,
          66.3,
          66.16,
          70.77,
          72.91,
          74.68,
          77.64,
          82.35,
          83.9,
          86.34,
          90.9,
          93.45,
          95.62,
          97.24,
          101.56,
          101.2,
          103.15,
          104.47,
          107.06,
          107.69,
          109.18,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "India",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          24.75,
          24.5,
          25.22,
          25.87,
          24.35,
          24.11,
          26.02,
          27.39,
          28.38,
          30.22,
          30.65,
          28.9,
          31.43,
          29.94,
          33.5,
          32.72,
          35.63,
          37.19,
          34.59,
          35.65,
          38.38,
          37.36,
          42.16,
          42.75,
          43.37,
          43.16,
          42.38,
          47.66,
          50.94,
          50.88,
          53.36,
          55.67,
          57.02,
          58.92,
          60.03,
          62.35,
          63.59,
          64.52,
          67.45,
          65.93,
          67.67,
          60.9,
          68.98,
          67.24,
          71.18,
          75.35,
          82.29,
          82.79,
          79.84,
          87.96,
          94.29,
          95.71,
          100,
          101.28,
          97.71,
          101,
          107.38,
          110.94,
          112.34,
          115.75,
          120.6,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Namibia",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          24.6,
          26.12,
          26.38,
          27.87,
          28.73,
          29.31,
          29.89,
          30.39,
          30.94,
          31.25,
          31.84,
          32.29,
          33.14,
          33.49,
          34.39,
          34.62,
          35.55,
          35.96,
          36.66,
          37.05,
          38.08,
          38.77,
          39.96,
          41.34,
          38.89,
          41.47,
          41.24,
          43.5,
          45.71,
          46.82,
          48.03,
          34.06,
          41.48,
          49.36,
          45.61,
          50.56,
          64.48,
          61.58,
          56.48,
          65.56,
          69.52,
          66.92,
          70.88,
          82.79,
          82.12,
          94.05,
          87.42,
          85.81,
          86.25,
          91.1,
          92.45,
          99.67,
          91.12,
          100.72,
          103.3,
          95.98,
          108.31,
          111.27,
          98.7,
          115.51,
          118.17,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(128, 0, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Russian Federation",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          86.46,
          80.96,
          67.86,
          66.6,
          67.3,
          74.88,
          52.4,
          56.93,
          63.36,
          70.94,
          72.14,
          66.54,
          71.94,
          74.37,
          75.2,
          76.2,
          89.66,
          85.65,
          61.78,
          92.23,
          77.84,
          90.73,
          96.87,
          99.64,
          103.49,
          110.09,
          103.57,
          111.49,
          112.75,
          111.63,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(219, 64, 82, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "United States",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          36.9,
          37.2,
          38.71,
          37.23,
          40.77,
          40.08,
          42.46,
          43.8,
          44.38,
          42.19,
          48.34,
          47.93,
          51.42,
          46.97,
          53.38,
          53.26,
          57.74,
          58.52,
          64.95,
          58.56,
          67.35,
          67.98,
          49.84,
          64.34,
          68.61,
          62.61,
          62.54,
          53.09,
          62.67,
          67.17,
          65.11,
          73.53,
          62.86,
          78.65,
          67.22,
          74.56,
          78.1,
          77.55,
          77.8,
          79.88,
          77.73,
          74.57,
          77.93,
          87.3,
          84.04,
          80.84,
          86.81,
          86.09,
          89.74,
          89.55,
          87,
          85.99,
          92.94,
          97.81,
          95.48,
          106.71,
          100.53,
          100.21,
          93.69,
          98.44,
          100.85,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(0, 128, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "World",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          ""
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "Crop Index (1960-2020)"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Metric Tons"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"805a2a8a-8cbc-4baf-9b0d-28f2e3f50cf0\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"805a2a8a-8cbc-4baf-9b0d-28f2e3f50cf0\")) {                    Plotly.newPlot(                        \"805a2a8a-8cbc-4baf-9b0d-28f2e3f50cf0\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"China\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",14.28,15.01,15.45,16.24,17.7,19.1,19.26,19.15,19.41,20.79,21.32,20.62,23.41,23.31,23.79,23.41,23.99,26.45,26.88,26.6,27.81,30.44,32.83,35.38,34.15,34.85,36.72,36.73,37.51,40.21,41.45,42.83,45.64,46.5,49.73,53.59,54.9,56.59,58.59,62.15,63.47,66.3,66.16,70.77,72.91,74.68,77.64,82.35,83.9,86.34,90.9,93.45,95.62,97.24,101.56,101.2,103.15,104.47,107.06,107.69,109.18,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"India\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",24.75,24.5,25.22,25.87,24.35,24.11,26.02,27.39,28.38,30.22,30.65,28.9,31.43,29.94,33.5,32.72,35.63,37.19,34.59,35.65,38.38,37.36,42.16,42.75,43.37,43.16,42.38,47.66,50.94,50.88,53.36,55.67,57.02,58.92,60.03,62.35,63.59,64.52,67.45,65.93,67.67,60.9,68.98,67.24,71.18,75.35,82.29,82.79,79.84,87.96,94.29,95.71,100.0,101.28,97.71,101.0,107.38,110.94,112.34,115.75,120.6,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Namibia\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",24.6,26.12,26.38,27.87,28.73,29.31,29.89,30.39,30.94,31.25,31.84,32.29,33.14,33.49,34.39,34.62,35.55,35.96,36.66,37.05,38.08,38.77,39.96,41.34,38.89,41.47,41.24,43.5,45.71,46.82,48.03,34.06,41.48,49.36,45.61,50.56,64.48,61.58,56.48,65.56,69.52,66.92,70.88,82.79,82.12,94.05,87.42,85.81,86.25,91.1,92.45,99.67,91.12,100.72,103.3,95.98,108.31,111.27,98.7,115.51,118.17,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(128, 0, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Russian Federation\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",86.46,80.96,67.86,66.6,67.3,74.88,52.4,56.93,63.36,70.94,72.14,66.54,71.94,74.37,75.2,76.2,89.66,85.65,61.78,92.23,77.84,90.73,96.87,99.64,103.49,110.09,103.57,111.49,112.75,111.63,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(219, 64, 82, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"United States\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",36.9,37.2,38.71,37.23,40.77,40.08,42.46,43.8,44.38,42.19,48.34,47.93,51.42,46.97,53.38,53.26,57.74,58.52,64.95,58.56,67.35,67.98,49.84,64.34,68.61,62.61,62.54,53.09,62.67,67.17,65.11,73.53,62.86,78.65,67.22,74.56,78.1,77.55,77.8,79.88,77.73,74.57,77.93,87.3,84.04,80.84,86.81,86.09,89.74,89.55,87.0,85.99,92.94,97.81,95.48,106.71,100.53,100.21,93.69,98.44,100.85,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(0, 128, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"World\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Crop Index (1960-2020)\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Metric Tons\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('805a2a8a-8cbc-4baf-9b0d-28f2e3f50cf0');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y = {\"AG.PRD.CROP.XD\":\"Crop index\"}\n",
    "\n",
    "x=[\"NAM\",\"USA\",\"IND\",\"CHN\",\"RUS\",\"WLD\"]\n",
    "\n",
    "geo = (fix_date_index(wbdata.get_dataframe(y,country=x)).squeeze().unstack('country'))\n",
    "geo.iplot(xTitle=\"Year\",yTitle=\"Metric Tons\", title=\"Crop Index (1960-2020)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Permanent Cropland: Namibia and the World"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "China",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          0.186403216786941,
          0.191729022980854,
          0.197054829174766,
          0.202380635368679,
          0.207706441562592,
          0.213032247756504,
          0.221553537666764,
          0.230074827577024,
          0.238596117487285,
          0.247117407397545,
          0.255638697307805,
          0.264159987218065,
          0.272681277128325,
          0.281202567038585,
          0.289723856948846,
          0.298245146859106,
          0.306766436769366,
          0.315287726679626,
          0.324661145580912,
          0.333395467738929,
          0.341916757649189,
          0.351503208798232,
          0.372806433573882,
          0.404761270737358,
          0.521929007003435,
          0.639096743269512,
          0.745612867147764,
          0.77756770431124,
          0.798870929086891,
          0.798870929086891,
          0.798870929086891,
          0.830825766250366,
          0.926690277740793,
          0.990599952067744,
          1.10989919303299,
          1.13972495347898,
          1.17167985871671,
          1.17167985871671,
          1.17167985871671,
          1.17168110674867,
          1.17168183060842,
          1.19298526369214,
          1.23559194605806,
          1.27819859211751,
          1.31547948247184,
          1.34210867897585,
          1.41134453436005,
          1.44862533338088,
          1.49123192906508,
          1.54449021224598,
          1.61905180869923,
          1.6829617485163,
          1.70426506178866,
          1.7063953931159,
          1.70426506178866,
          1.77527629867674,
          1.84628734338069,
          1.91729839873629,
          1.99186000313159,
          2.0131633186731,
          2.02381497644386,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "India",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          1.74223645310256,
          1.91713277658004,
          1.54043300293624,
          1.4751832207158,
          1.41867825466923,
          1.3890804153115,
          1.34871972527824,
          1.5135258762474,
          1.5135258762474,
          1.5135258762474,
          1.61442760133056,
          1.61442760133056,
          1.68169541805266,
          1.68169541805266,
          1.68169541805266,
          1.68169541805266,
          1.68169541805266,
          1.68169541805266,
          1.68169541805266,
          1.78259714313582,
          1.84986495985793,
          1.84986495985793,
          1.95076668494109,
          1.95076668494109,
          1.95076668494109,
          2.0180345016632,
          2.18620404346846,
          2.18620404346846,
          2.18620404346846,
          2.23665490601004,
          2.35437358527373,
          2.45527531035689,
          2.5898109438011,
          2.62344485216216,
          2.69071266888426,
          2.85888221068953,
          2.85888221068953,
          2.89924290072279,
          3.07750261503638,
          3.0943195692169,
          3.19522129430006,
          3.22885520266111,
          3.36339083610533,
          3.43402204366354,
          3.44074882533575,
          3.63246210299375,
          3.76027095476576,
          3.83426555316007,
          3.96880118660429,
          4.11174529713876,
          4.1672412459345,
          4.30514027021482,
          4.37240808693693,
          4.37240808693693,
          4.37240808693693,
          4.37240808693693,
          4.37240808693693,
          4.47330981202009,
          4.47330981202009,
          4.57421153710325,
          4.57421153710325,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Namibia",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.00121463882714475,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.0024292776542895,
          0.00364391648143425,
          0.00485855530857899,
          0.00485855530857899,
          0.00485855530857899,
          0.00485855530857899,
          0.00485855530857899,
          0.00485855530857899,
          0.00485855530857899,
          0.00485855530857899,
          0.00607319413572374,
          0.00607319413572374,
          0.00728783296286849,
          0.00850247179001324,
          0.00971711061715799,
          0.00971711061715799,
          0.00971711061715799,
          0.0109317494443027,
          0.0109317494443027,
          0.0109317494443027,
          0.0109317494443027,
          0.0109317494443027,
          0.0121463882714475,
          0.0121463882714475,
          0.0133610270985922,
          0.0133610270985922,
          0.0133610270985922,
          0.0133610270985922,
          0.014575665925737,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(128, 0, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Russian Federation",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          0.103722097992977,
          0.107224502599141,
          0.120991396913437,
          0.116006589174265,
          0.119001389672462,
          0.117103668495267,
          0.111529609982114,
          0.112578873857355,
          0.113788005132669,
          0.11342796652593,
          0.112020433503816,
          0.110738185383292,
          0.110492313458757,
          0.109880785452272,
          0.109722098409182,
          0.10953892295274,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          0.109483680336963,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(219, 64, 82, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "United States",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          0.205154296994419,
          0.207010402927843,
          0.204062469974757,
          0.204499200782622,
          0.204499200782622,
          0.201442085127569,
          0.198712517578415,
          0.195982950029261,
          0.193253382480107,
          0.192707468970276,
          0.192161555460445,
          0.191615641950614,
          0.191069728440784,
          0.190632997632919,
          0.190632997632919,
          0.190632997632919,
          0.190087084123088,
          0.204062469974757,
          0.204062469974757,
          0.204062469974757,
          0.204062469974757,
          0.222077615799174,
          0.222077615799174,
          0.222077615799174,
          0.222077615799174,
          0.222077615799174,
          0.222077615799174,
          0.222077615799174,
          0.223824539030632,
          0.22928367412894,
          0.22928367412894,
          0.22928367412894,
          0.240201944325557,
          0.240201944325557,
          0.251120214522173,
          0.251120214522173,
          0.272956754915405,
          0.272956754915405,
          0.294793295308638,
          0.29469805455625,
          0.29469805455625,
          0.297972477384653,
          0.297972477384653,
          0.29469805455625,
          0.29469805455625,
          0.29469805455625,
          0.29469805455625,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          0.295165194120309,
          ""
         ]
        },
        {
         "line": {
          "color": "rgba(0, 128, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "World",
         "text": "",
         "type": "scatter",
         "x": [
          1960,
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021,
          2022
         ],
         "y": [
          "",
          0.690182844373511,
          0.705553894234019,
          0.705614626202685,
          0.716089775156475,
          0.720769497633433,
          0.725255955993498,
          0.728918955605208,
          0.73836244217381,
          0.746975907993893,
          0.756846137672341,
          0.766370902234025,
          0.774647845531192,
          0.787788661792951,
          0.798271895663027,
          0.80811852648498,
          0.819958180805672,
          0.83201873684669,
          0.843415263135632,
          0.855999190101234,
          0.870930809203688,
          0.881256358723666,
          0.887682395093639,
          0.887382449813542,
          0.896381477867236,
          0.918713018348705,
          0.943603850646089,
          0.973122528711264,
          0.99434347076635,
          1.00426957520997,
          1.0255466808634,
          1.03410783105564,
          0.908563439637893,
          0.928535578616912,
          0.951144238388752,
          0.960032384104634,
          0.970151331664033,
          0.981995789736223,
          0.992813253701463,
          1.015089165436,
          1.02875846381281,
          1.04682581188414,
          1.05758231664174,
          1.07402025819221,
          1.09508962528601,
          1.11918648143536,
          1.14269713518456,
          1.16765892120195,
          1.1800324659852,
          1.1966302253113,
          1.21975072738682,
          1.23915438891804,
          1.25433370354785,
          1.27210736188251,
          1.28352254257891,
          1.30634792609171,
          1.31333717209052,
          1.34487898194579,
          1.37457977654063,
          1.3933981487774,
          1.4036796501666,
          1.41707626324144,
          ""
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "Total Percentange of Permanent Cropland (1960-2020)"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Percentage of Land Area(%)"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"c55855cf-2eb8-4b41-a974-dbb5ac9e8108\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"c55855cf-2eb8-4b41-a974-dbb5ac9e8108\")) {                    Plotly.newPlot(                        \"c55855cf-2eb8-4b41-a974-dbb5ac9e8108\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"China\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",0.186403216786941,0.191729022980854,0.197054829174766,0.202380635368679,0.207706441562592,0.213032247756504,0.221553537666764,0.230074827577024,0.238596117487285,0.247117407397545,0.255638697307805,0.264159987218065,0.272681277128325,0.281202567038585,0.289723856948846,0.298245146859106,0.306766436769366,0.315287726679626,0.324661145580912,0.333395467738929,0.341916757649189,0.351503208798232,0.372806433573882,0.404761270737358,0.521929007003435,0.639096743269512,0.745612867147764,0.77756770431124,0.798870929086891,0.798870929086891,0.798870929086891,0.830825766250366,0.926690277740793,0.990599952067744,1.10989919303299,1.13972495347898,1.17167985871671,1.17167985871671,1.17167985871671,1.17168110674867,1.17168183060842,1.19298526369214,1.23559194605806,1.27819859211751,1.31547948247184,1.34210867897585,1.41134453436005,1.44862533338088,1.49123192906508,1.54449021224598,1.61905180869923,1.6829617485163,1.70426506178866,1.7063953931159,1.70426506178866,1.77527629867674,1.84628734338069,1.91729839873629,1.99186000313159,2.0131633186731,2.02381497644386,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"India\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",1.74223645310256,1.91713277658004,1.54043300293624,1.4751832207158,1.41867825466923,1.3890804153115,1.34871972527824,1.5135258762474,1.5135258762474,1.5135258762474,1.61442760133056,1.61442760133056,1.68169541805266,1.68169541805266,1.68169541805266,1.68169541805266,1.68169541805266,1.68169541805266,1.68169541805266,1.78259714313582,1.84986495985793,1.84986495985793,1.95076668494109,1.95076668494109,1.95076668494109,2.0180345016632,2.18620404346846,2.18620404346846,2.18620404346846,2.23665490601004,2.35437358527373,2.45527531035689,2.5898109438011,2.62344485216216,2.69071266888426,2.85888221068953,2.85888221068953,2.89924290072279,3.07750261503638,3.0943195692169,3.19522129430006,3.22885520266111,3.36339083610533,3.43402204366354,3.44074882533575,3.63246210299375,3.76027095476576,3.83426555316007,3.96880118660429,4.11174529713876,4.1672412459345,4.30514027021482,4.37240808693693,4.37240808693693,4.37240808693693,4.37240808693693,4.37240808693693,4.47330981202009,4.47330981202009,4.57421153710325,4.57421153710325,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Namibia\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.00121463882714475,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.0024292776542895,0.00364391648143425,0.00485855530857899,0.00485855530857899,0.00485855530857899,0.00485855530857899,0.00485855530857899,0.00485855530857899,0.00485855530857899,0.00485855530857899,0.00607319413572374,0.00607319413572374,0.00728783296286849,0.00850247179001324,0.00971711061715799,0.00971711061715799,0.00971711061715799,0.0109317494443027,0.0109317494443027,0.0109317494443027,0.0109317494443027,0.0109317494443027,0.0121463882714475,0.0121463882714475,0.0133610270985922,0.0133610270985922,0.0133610270985922,0.0133610270985922,0.014575665925737,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(128, 0, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Russian Federation\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",0.103722097992977,0.107224502599141,0.120991396913437,0.116006589174265,0.119001389672462,0.117103668495267,0.111529609982114,0.112578873857355,0.113788005132669,0.11342796652593,0.112020433503816,0.110738185383292,0.110492313458757,0.109880785452272,0.109722098409182,0.10953892295274,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,0.109483680336963,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(219, 64, 82, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"United States\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",0.205154296994419,0.207010402927843,0.204062469974757,0.204499200782622,0.204499200782622,0.201442085127569,0.198712517578415,0.195982950029261,0.193253382480107,0.192707468970276,0.192161555460445,0.191615641950614,0.191069728440784,0.190632997632919,0.190632997632919,0.190632997632919,0.190087084123088,0.204062469974757,0.204062469974757,0.204062469974757,0.204062469974757,0.222077615799174,0.222077615799174,0.222077615799174,0.222077615799174,0.222077615799174,0.222077615799174,0.222077615799174,0.223824539030632,0.22928367412894,0.22928367412894,0.22928367412894,0.240201944325557,0.240201944325557,0.251120214522173,0.251120214522173,0.272956754915405,0.272956754915405,0.294793295308638,0.29469805455625,0.29469805455625,0.297972477384653,0.297972477384653,0.29469805455625,0.29469805455625,0.29469805455625,0.29469805455625,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,0.295165194120309,\"\"],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(0, 128, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"World\",\"text\":\"\",\"x\":[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],\"y\":[\"\",0.690182844373511,0.705553894234019,0.705614626202685,0.716089775156475,0.720769497633433,0.725255955993498,0.728918955605208,0.73836244217381,0.746975907993893,0.756846137672341,0.766370902234025,0.774647845531192,0.787788661792951,0.798271895663027,0.80811852648498,0.819958180805672,0.83201873684669,0.843415263135632,0.855999190101234,0.870930809203688,0.881256358723666,0.887682395093639,0.887382449813542,0.896381477867236,0.918713018348705,0.943603850646089,0.973122528711264,0.99434347076635,1.00426957520997,1.0255466808634,1.03410783105564,0.908563439637893,0.928535578616912,0.951144238388752,0.960032384104634,0.970151331664033,0.981995789736223,0.992813253701463,1.015089165436,1.02875846381281,1.04682581188414,1.05758231664174,1.07402025819221,1.09508962528601,1.11918648143536,1.14269713518456,1.16765892120195,1.1800324659852,1.1966302253113,1.21975072738682,1.23915438891804,1.25433370354785,1.27210736188251,1.28352254257891,1.30634792609171,1.31333717209052,1.34487898194579,1.37457977654063,1.3933981487774,1.4036796501666,1.41707626324144,\"\"],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Total Percentange of Permanent Cropland (1960-2020)\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Percentage of Land Area(%)\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('c55855cf-2eb8-4b41-a974-dbb5ac9e8108');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "vars = {\"AG.LND.CROP.ZS\":\"Permanent Cropland\"}\n",
    "\n",
    "users = [\"NAM\",\"USA\",\"IND\",\"CHN\",\"RUS\",\"WLD\"]\n",
    "\n",
    "geo = (fix_date_index(wbdata.get_dataframe(vars,country=users)).squeeze().unstack('country'))\n",
    "geo.iplot(xTitle=\"Year\",yTitle=\"Percentage of Land Area(%)\", title=\"Total Percentange of Permanent Cropland (1960-2020)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### FAO Food Index: Namibia and South Africa\n",
    "The FAO compiles a series of data meant to measure changes in the supply of food of all sorts, including both plant and animal sources.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Livestock index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.22119917662781963,
          0.23005738954491364,
          0.24032927862092138,
          0.2478004436885952,
          0.27901208934392285,
          0.29000532029804765,
          0.2879837223693085,
          0.30500071389362526,
          0.3357573429701651,
          0.3376257147410338,
          0.3432214411988837,
          0.3793422144365213,
          0.38323654709818095,
          0.38303370959071603,
          0.415243349845085,
          0.4355119109620965,
          0.4628808647686473,
          0.49160008112308573,
          0.5336478363930298,
          0.5318493666817935,
          0.5177854569434437,
          0.5770074489699595,
          0.6104031164181661,
          0.6349658951910468,
          0.6560772585512017,
          0.643343811915577,
          0.6733014323849706,
          0.6834305248050815,
          0.7094906981298292,
          0.8287679239317728,
          0.911887771675451,
          0.9203159477027781,
          0.8882722186423619,
          0.8215169494234594,
          0.8275485465029551,
          0.8328737443524297,
          1.0578797144961516,
          0.8919460993306652,
          0.9716022461507101,
          1,
          1.0346285540035283,
          1.056444823928844,
          1.1190333190401376,
          1.1797224053161963,
          1.2640452423738673,
          1.3594111560763662,
          1.4591165069345107,
          1.5257139618795037,
          1.5547349270591813,
          1.6913115911964733,
          1.6808921139618205,
          1.7411249875522536,
          1.892930953569369,
          2.022744341088228,
          2.130431014759073,
          2.1236788847603734,
          2.035507335212036,
          2.111884738723,
          2.248981059930982,
          2.3064871837144665,
          2.3251792703533822
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Food index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.16429583597910669,
          0.17236369307171998,
          0.18623095926678146,
          0.18548563464381362,
          0.2006416521613747,
          0.21739989620078973,
          0.26772911901148916,
          0.243447698789785,
          0.26501740029274345,
          0.26681350900020423,
          0.3101962437913205,
          0.34266016434791724,
          0.30452850414859395,
          0.3733585657145922,
          0.3746621747249507,
          0.3855060865438996,
          0.41770349551544445,
          0.44992890855857026,
          0.4576684029479869,
          0.4868774243331225,
          0.5442428299034501,
          0.51561775890101,
          0.47002314039958154,
          0.522203462138251,
          0.5682979315393625,
          0.5780224922968399,
          0.6298287536438331,
          0.657891062664386,
          0.715612925613332,
          0.7360692906931259,
          0.7857278824734596,
          0.6878287097673516,
          0.7785605428122085,
          0.8082631913715478,
          0.7294997095834211,
          0.8604437814540669,
          0.9605570254767756,
          0.8608043220131526,
          0.9410010893531439,
          1,
          0.9660728093343255,
          1.0351481075278466,
          1.050969598382031,
          1.085336463538172,
          1.1626025612378954,
          1.1396838162760141,
          1.1820689034692193,
          1.3450761177087136,
          1.342579223092384,
          1.3997379013756224,
          1.4046234430190099,
          1.4704873788018253,
          1.575401437600298,
          1.691626151051472,
          1.6941963913413776,
          1.6272314226944389,
          1.8000291212567487,
          1.7958855524046125,
          1.823131556589007,
          1.9664998458529726,
          2.0383098057995843
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Crop index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.14263243787607016,
          0.14988460440769044,
          0.16787744224238577,
          0.1614017939750488,
          0.16831093747037784,
          0.18850633972993178,
          0.27360924430977285,
          0.22415334501790335,
          0.24137288788312725,
          0.2433913120712065,
          0.3070832958672639,
          0.3353102268121724,
          0.26729713738351474,
          0.3869448330726539,
          0.366959086830603,
          0.3681891840624558,
          0.4066481060106194,
          0.4451201973015038,
          0.429444592815747,
          0.4819178773956793,
          0.5867653482736346,
          0.49617585396205943,
          0.39657675493683214,
          0.46748993879724465,
          0.5325598307749425,
          0.5565008561965332,
          0.6231946204452607,
          0.6698582140786067,
          0.7524452960598944,
          0.6976064212732398,
          0.7217701400904761,
          0.5399719630649896,
          0.7100522984008139,
          0.8117317601919359,
          0.6716455713082493,
          0.8893132368769582,
          0.8905359729398759,
          0.847780739874236,
          0.9296775923546455,
          1,
          0.9218654915126672,
          1.0158326822281771,
          0.9952557503329684,
          1.0097340915832607,
          1.0809496898144315,
          0.9649490132295621,
          0.9642258337018402,
          1.1888674277356732,
          1.16269737705017,
          1.1617417956727196,
          1.1805389833028346,
          1.2463203921771056,
          1.3133017396695223,
          1.4167648176216547,
          1.3497928337382836,
          1.2377530085468753,
          1.5938636174355676,
          1.5396375873580057,
          1.490160316172322,
          1.6882441064738678,
          1.7879871697198113
         ]
        },
        {
         "line": {
          "color": "rgba(128, 0, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Population",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.3629198612205352,
          0.3738925842089292,
          0.38540816613820533,
          0.39738942803093463,
          0.40986659636180905,
          0.42273852458830796,
          0.43600198712903304,
          0.4496703989847664,
          0.46363383405037367,
          0.4778198128709926,
          0.49198534876844524,
          0.506234856589583,
          0.5208462276483764,
          0.5356818300180124,
          0.5506551070373941,
          0.56565803377188,
          0.5810284204481695,
          0.5969129562547505,
          0.6130102949877498,
          0.6293846064916727,
          0.6458118303474062,
          0.6626843126048928,
          0.6806868805094692,
          0.6999769467056625,
          0.7210128000896157,
          0.7450416725891331,
          0.7715619115316585,
          0.7987875274500181,
          0.82601978678437,
          0.8518433642292764,
          0.8739180684381218,
          0.8920709569804423,
          0.9084057497718703,
          0.9242675356169339,
          0.9396072472277409,
          0.9540373235227809,
          0.967355022826222,
          0.9794694948222583,
          0.9904175666786419,
          1,
          1.0088959398816566,
          1.018119820992622,
          1.0275729960819227,
          1.0372288701241226,
          1.0470781295199527,
          1.0572164736380496,
          1.0679898727852057,
          1.080159884593397,
          1.0930828667241461,
          1.1062018403074034,
          1.1202663151082004,
          1.1352558268419042,
          1.1508194279800943,
          1.169103454563499,
          1.1936040523214082,
          1.2052624997367198,
          1.2099392723421605,
          1.2248586757437518,
          1.2408246628210047,
          1.2560953768959422,
          1.2687056485227928
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "FAO Food Index in South Africa"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Index"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"12d50ea2-6b27-417a-b4e5-6db254b21834\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"12d50ea2-6b27-417a-b4e5-6db254b21834\")) {                    Plotly.newPlot(                        \"12d50ea2-6b27-417a-b4e5-6db254b21834\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Livestock index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.22119917662781963,0.23005738954491364,0.24032927862092138,0.2478004436885952,0.27901208934392285,0.29000532029804765,0.2879837223693085,0.30500071389362526,0.3357573429701651,0.3376257147410338,0.3432214411988837,0.3793422144365213,0.38323654709818095,0.38303370959071603,0.415243349845085,0.4355119109620965,0.4628808647686473,0.49160008112308573,0.5336478363930298,0.5318493666817935,0.5177854569434437,0.5770074489699595,0.6104031164181661,0.6349658951910468,0.6560772585512017,0.643343811915577,0.6733014323849706,0.6834305248050815,0.7094906981298292,0.8287679239317728,0.911887771675451,0.9203159477027781,0.8882722186423619,0.8215169494234594,0.8275485465029551,0.8328737443524297,1.0578797144961516,0.8919460993306652,0.9716022461507101,1.0,1.0346285540035283,1.056444823928844,1.1190333190401376,1.1797224053161963,1.2640452423738673,1.3594111560763662,1.4591165069345107,1.5257139618795037,1.5547349270591813,1.6913115911964733,1.6808921139618205,1.7411249875522536,1.892930953569369,2.022744341088228,2.130431014759073,2.1236788847603734,2.035507335212036,2.111884738723,2.248981059930982,2.3064871837144665,2.3251792703533822],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Food index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.16429583597910669,0.17236369307171998,0.18623095926678146,0.18548563464381362,0.2006416521613747,0.21739989620078973,0.26772911901148916,0.243447698789785,0.26501740029274345,0.26681350900020423,0.3101962437913205,0.34266016434791724,0.30452850414859395,0.3733585657145922,0.3746621747249507,0.3855060865438996,0.41770349551544445,0.44992890855857026,0.4576684029479869,0.4868774243331225,0.5442428299034501,0.51561775890101,0.47002314039958154,0.522203462138251,0.5682979315393625,0.5780224922968399,0.6298287536438331,0.657891062664386,0.715612925613332,0.7360692906931259,0.7857278824734596,0.6878287097673516,0.7785605428122085,0.8082631913715478,0.7294997095834211,0.8604437814540669,0.9605570254767756,0.8608043220131526,0.9410010893531439,1.0,0.9660728093343255,1.0351481075278466,1.050969598382031,1.085336463538172,1.1626025612378954,1.1396838162760141,1.1820689034692193,1.3450761177087136,1.342579223092384,1.3997379013756224,1.4046234430190099,1.4704873788018253,1.575401437600298,1.691626151051472,1.6941963913413776,1.6272314226944389,1.8000291212567487,1.7958855524046125,1.823131556589007,1.9664998458529726,2.0383098057995843],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Crop index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.14263243787607016,0.14988460440769044,0.16787744224238577,0.1614017939750488,0.16831093747037784,0.18850633972993178,0.27360924430977285,0.22415334501790335,0.24137288788312725,0.2433913120712065,0.3070832958672639,0.3353102268121724,0.26729713738351474,0.3869448330726539,0.366959086830603,0.3681891840624558,0.4066481060106194,0.4451201973015038,0.429444592815747,0.4819178773956793,0.5867653482736346,0.49617585396205943,0.39657675493683214,0.46748993879724465,0.5325598307749425,0.5565008561965332,0.6231946204452607,0.6698582140786067,0.7524452960598944,0.6976064212732398,0.7217701400904761,0.5399719630649896,0.7100522984008139,0.8117317601919359,0.6716455713082493,0.8893132368769582,0.8905359729398759,0.847780739874236,0.9296775923546455,1.0,0.9218654915126672,1.0158326822281771,0.9952557503329684,1.0097340915832607,1.0809496898144315,0.9649490132295621,0.9642258337018402,1.1888674277356732,1.16269737705017,1.1617417956727196,1.1805389833028346,1.2463203921771056,1.3133017396695223,1.4167648176216547,1.3497928337382836,1.2377530085468753,1.5938636174355676,1.5396375873580057,1.490160316172322,1.6882441064738678,1.7879871697198113],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(128, 0, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Population\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.3629198612205352,0.3738925842089292,0.38540816613820533,0.39738942803093463,0.40986659636180905,0.42273852458830796,0.43600198712903304,0.4496703989847664,0.46363383405037367,0.4778198128709926,0.49198534876844524,0.506234856589583,0.5208462276483764,0.5356818300180124,0.5506551070373941,0.56565803377188,0.5810284204481695,0.5969129562547505,0.6130102949877498,0.6293846064916727,0.6458118303474062,0.6626843126048928,0.6806868805094692,0.6999769467056625,0.7210128000896157,0.7450416725891331,0.7715619115316585,0.7987875274500181,0.82601978678437,0.8518433642292764,0.8739180684381218,0.8920709569804423,0.9084057497718703,0.9242675356169339,0.9396072472277409,0.9540373235227809,0.967355022826222,0.9794694948222583,0.9904175666786419,1.0,1.0088959398816566,1.018119820992622,1.0275729960819227,1.0372288701241226,1.0470781295199527,1.0572164736380496,1.0679898727852057,1.080159884593397,1.0930828667241461,1.1062018403074034,1.1202663151082004,1.1352558268419042,1.1508194279800943,1.169103454563499,1.1936040523214082,1.2052624997367198,1.2099392723421605,1.2248586757437518,1.2408246628210047,1.2560953768959422,1.2687056485227928],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"FAO Food Index in South Africa\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Index\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('12d50ea2-6b27-417a-b4e5-6db254b21834');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "vars = {\"AG.PRD.LVSK.XD\":\"Livestock index\",\n",
    "        \"AG.PRD.FOOD.XD\":\"Food index\",\n",
    "        \"AG.PRD.CROP.XD\":\"Crop index\",\n",
    "        \"SP.POP.TOTL\":\"Population\"}\n",
    "\n",
    "use=[\"ZAF\"]\n",
    "\n",
    "food = fix_date_index(wbdata.get_dataframe(vars, country = use)).dropna()\n",
    "# Add population back...\n",
    "Population = food.Population\n",
    "\n",
    "# Weight indices by population\n",
    "food = food.filter(regex='index$').multiply(Population,axis=0)\n",
    "\n",
    "food['Population'] = Population\n",
    "\n",
    "# No \"WLD\" or other regions; add up all countries\n",
    "food = food.groupby('date').sum().replace(0,np.nan).dropna()\n",
    "\n",
    "food.sort_index(inplace=True)\n",
    "\n",
    "# Normalize so 2000 = 1\n",
    "food = food/food.loc[2000,:]\n",
    "\n",
    "food.iplot(xTitle=\"Year\", yTitle=\"Index\", title=\"FAO Food Index in South Africa\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And here in growth rates:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Livestock index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          0.039265250214939096,
          0.043681179712883766,
          0.03061378243262025,
          0.11863135216009257,
          0.03864415680316524,
          -0.006995309679929562,
          0.05741015825186557,
          0.09607458827513948,
          0.00554922356303944,
          0.01643791094039937,
          0.10006289812457525,
          0.01021367683577723,
          -0.0005294150736817604,
          0.0807417336382158,
          0.04765741246075805,
          0.06094756345741348,
          0.06019583324920241,
          0.08207059628561164,
          -0.0033758350824986127,
          -0.026799323233316352,
          0.1082941955712432,
          0.056264409240174285,
          0.03945170359822758,
          0.03270726510141014,
          -0.019599273141351625,
          0.04551384190885305,
          0.01493188181378352,
          0.03742238128335984,
          0.15539278288066688,
          0.09557675619223094,
          0.00920010737476945,
          -0.035438783963784456,
          -0.07812567898862617,
          0.007315202448134439,
          0.006414291276061079,
          0.23913985127708715,
          -0.17061621055748888,
          0.08554080493645053,
          0.02880877005079131,
          0.03404247728194561,
          0.020866854088762557,
          0.05755587324424363,
          0.052813956455025846,
          0.06903792703143335,
          0.07273454441321048,
          0.07077948780257814,
          0.04463135190825168,
          0.018842593961241605,
          0.08419925121195498,
          -0.006179644709452647,
          0.03520677618760826,
          0.08359494807838952,
          0.06632877711389296,
          0.05186913952835093,
          -0.0031744058466751657,
          -0.04240481515497496,
          0.03683569729071123,
          0.06289646150385508,
          0.025248416015308695,
          0.008071474189515815
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Food index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          0.047938058307385845,
          0.07738088088980866,
          -0.004010182133428186,
          0.07854305409174756,
          0.08021800536246104,
          0.20823722217180207,
          -0.09507358931375554,
          0.0848933552248794,
          0.006754460881036373,
          0.1506551954854951,
          0.09953403984940357,
          -0.117974489076353,
          0.20377456762043067,
          0.0034854924727102388,
          0.028532229033497614,
          0.08021485837246967,
          0.0743177493517585,
          0.017055321557925884,
          0.06186748512642326,
          0.11138312977023712,
          -0.05402981211084612,
          -0.09258378526200761,
          0.1052753577667791,
          0.08458852241118198,
          0.016966973360826088,
          0.0858351808993475,
          0.043591396535255955,
          0.08410005473665055,
          0.028184845166128958,
          0.06528626772073753,
          -0.13307068840757263,
          0.12390691822097305,
          0.03744098058231732,
          -0.10252876751830137,
          0.16508931123989756,
          0.11006506996330306,
          -0.10964614074138274,
          0.08907708691850985,
          0.06081098174265188,
          -0.034516075628240744,
          0.06906059116860055,
          0.015168649563130132,
          0.03217687845990249,
          0.06877103574518036,
          -0.01991020951578984,
          0.036515341459286865,
          0.1291843932923844,
          -0.0018580472702495188,
          0.04169244851728343,
          0.0034842489864493897,
          0.04582464126740704,
          0.06891622477166626,
          0.0711801650385655,
          0.001518237150018309,
          -0.040328465981143535,
          0.10092278622276935,
          -0.0023045990030974295,
          0.015057413735646064,
          0.0756995765234676,
          0.03586570336621919
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Crop index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          0.04959473738286779,
          0.11336850863764014,
          -0.03933733185791022,
          0.04191621616446661,
          0.11331855181645056,
          0.37256933401748604,
          -0.19937057924694557,
          0.07401259674308736,
          0.008327495522943762,
          0.23244854695062456,
          0.08793712066148318,
          -0.22669523978023776,
          0.3699212189581973,
          -0.05303177085407018,
          0.0033465313830485233,
          0.0993513138624651,
          0.09039614492949721,
          -0.03585162280845511,
          0.1152809915061761,
          0.19685127181609574,
          -0.16769458433613094,
          -0.22406080464943545,
          0.16450822368997253,
          0.13031742232682697,
          0.0439734597179946,
          0.11319015311845099,
          0.07220720684086457,
          0.11626222850263179,
          -0.07567322035537916,
          0.03405164531887822,
          -0.2901895047177092,
          0.2738214090816753,
          0.13383131395259876,
          -0.18943916325673835,
          0.2807187431593354,
          0.0013739773555330181,
          -0.04920145736274012,
          0.09221581026413109,
          0.07291742782794397,
          -0.08135595379848916,
          0.09706460654678808,
          -0.02046419208928956,
          0.014442559870900044,
          0.06815297663194146,
          -0.1135200122324162,
          -0.000749729411770754,
          0.20943085701376382,
          -0.02225848175436182,
          -0.000822203861040316,
          0.016050672786813408,
          0.05422442418721485,
          0.05234885437313036,
          0.07583159663212385,
          -0.048424850710782175,
          -0.08665347827013642,
          0.2528633708405798,
          -0.03461396090897173,
          -0.0326633469300045,
          0.12480528964231258,
          0.05740150239535313
         ]
        },
        {
         "line": {
          "color": "rgba(128, 0, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Population",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          0.029786506260395584,
          0.030334396325203183,
          0.03061378243262003,
          0.03091500510249301,
          0.030922110709255213,
          0.030892958239573165,
          0.030868066719664022,
          0.03058022223567125,
          0.030138610973662106,
          0.029215236219940155,
          0.02855176794090053,
          0.028454144656994695,
          0.02808553438660577,
          0.027568289022149806,
          0.026881041867839683,
          0.026809957092094883,
          0.026971628754560162,
          0.02661042938458158,
          0.02636079666951341,
          0.02576565016092841,
          0.0257905498141367,
          0.02680367986684945,
          0.02794499448332949,
          0.029609489148854085,
          0.0327832628041107,
          0.034976763665856836,
          0.03467807046882945,
          0.03352374086770249,
          0.030783936947649082,
          0.025583962929086296,
          0.02055904954501639,
          0.01814546217032173,
          0.017310430672934862,
          0.01646039541009811,
          0.015240828018564988,
          0.013862772595190684,
          0.01244552680994723,
          0.011115545448797995,
          0.009628640255708814,
          0.008856604122043922,
          0.009101009430225347,
          0.009242093728086959,
          0.009352901688879499,
          0.00945094240817701,
          0.009635934578021081,
          0.010138772126754889,
          0.011330813387091673,
          0.011892950701332769,
          0.011930360036350882,
          0.012634056181142841,
          0.0132915852455181,
          0.013616211070757583,
          0.01576294221325658,
          0.020740168585351354,
          0.009720039820643483,
          0.0038727848785737318,
          0.012255300399433983,
          0.012950738629212838,
          0.012231792951145182,
          0.009989204185630624
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "FAO Food Index Growth Rates in South Africa"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Growth rates"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"422a7cbf-a458-4e50-a46d-422afaf03bb1\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"422a7cbf-a458-4e50-a46d-422afaf03bb1\")) {                    Plotly.newPlot(                        \"422a7cbf-a458-4e50-a46d-422afaf03bb1\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Livestock index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",0.039265250214939096,0.043681179712883766,0.03061378243262025,0.11863135216009257,0.03864415680316524,-0.006995309679929562,0.05741015825186557,0.09607458827513948,0.00554922356303944,0.01643791094039937,0.10006289812457525,0.01021367683577723,-0.0005294150736817604,0.0807417336382158,0.04765741246075805,0.06094756345741348,0.06019583324920241,0.08207059628561164,-0.0033758350824986127,-0.026799323233316352,0.1082941955712432,0.056264409240174285,0.03945170359822758,0.03270726510141014,-0.019599273141351625,0.04551384190885305,0.01493188181378352,0.03742238128335984,0.15539278288066688,0.09557675619223094,0.00920010737476945,-0.035438783963784456,-0.07812567898862617,0.007315202448134439,0.006414291276061079,0.23913985127708715,-0.17061621055748888,0.08554080493645053,0.02880877005079131,0.03404247728194561,0.020866854088762557,0.05755587324424363,0.052813956455025846,0.06903792703143335,0.07273454441321048,0.07077948780257814,0.04463135190825168,0.018842593961241605,0.08419925121195498,-0.006179644709452647,0.03520677618760826,0.08359494807838952,0.06632877711389296,0.05186913952835093,-0.0031744058466751657,-0.04240481515497496,0.03683569729071123,0.06289646150385508,0.025248416015308695,0.008071474189515815],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Food index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",0.047938058307385845,0.07738088088980866,-0.004010182133428186,0.07854305409174756,0.08021800536246104,0.20823722217180207,-0.09507358931375554,0.0848933552248794,0.006754460881036373,0.1506551954854951,0.09953403984940357,-0.117974489076353,0.20377456762043067,0.0034854924727102388,0.028532229033497614,0.08021485837246967,0.0743177493517585,0.017055321557925884,0.06186748512642326,0.11138312977023712,-0.05402981211084612,-0.09258378526200761,0.1052753577667791,0.08458852241118198,0.016966973360826088,0.0858351808993475,0.043591396535255955,0.08410005473665055,0.028184845166128958,0.06528626772073753,-0.13307068840757263,0.12390691822097305,0.03744098058231732,-0.10252876751830137,0.16508931123989756,0.11006506996330306,-0.10964614074138274,0.08907708691850985,0.06081098174265188,-0.034516075628240744,0.06906059116860055,0.015168649563130132,0.03217687845990249,0.06877103574518036,-0.01991020951578984,0.036515341459286865,0.1291843932923844,-0.0018580472702495188,0.04169244851728343,0.0034842489864493897,0.04582464126740704,0.06891622477166626,0.0711801650385655,0.001518237150018309,-0.040328465981143535,0.10092278622276935,-0.0023045990030974295,0.015057413735646064,0.0756995765234676,0.03586570336621919],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Crop index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",0.04959473738286779,0.11336850863764014,-0.03933733185791022,0.04191621616446661,0.11331855181645056,0.37256933401748604,-0.19937057924694557,0.07401259674308736,0.008327495522943762,0.23244854695062456,0.08793712066148318,-0.22669523978023776,0.3699212189581973,-0.05303177085407018,0.0033465313830485233,0.0993513138624651,0.09039614492949721,-0.03585162280845511,0.1152809915061761,0.19685127181609574,-0.16769458433613094,-0.22406080464943545,0.16450822368997253,0.13031742232682697,0.0439734597179946,0.11319015311845099,0.07220720684086457,0.11626222850263179,-0.07567322035537916,0.03405164531887822,-0.2901895047177092,0.2738214090816753,0.13383131395259876,-0.18943916325673835,0.2807187431593354,0.0013739773555330181,-0.04920145736274012,0.09221581026413109,0.07291742782794397,-0.08135595379848916,0.09706460654678808,-0.02046419208928956,0.014442559870900044,0.06815297663194146,-0.1135200122324162,-0.000749729411770754,0.20943085701376382,-0.02225848175436182,-0.000822203861040316,0.016050672786813408,0.05422442418721485,0.05234885437313036,0.07583159663212385,-0.048424850710782175,-0.08665347827013642,0.2528633708405798,-0.03461396090897173,-0.0326633469300045,0.12480528964231258,0.05740150239535313],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(128, 0, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Population\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",0.029786506260395584,0.030334396325203183,0.03061378243262003,0.03091500510249301,0.030922110709255213,0.030892958239573165,0.030868066719664022,0.03058022223567125,0.030138610973662106,0.029215236219940155,0.02855176794090053,0.028454144656994695,0.02808553438660577,0.027568289022149806,0.026881041867839683,0.026809957092094883,0.026971628754560162,0.02661042938458158,0.02636079666951341,0.02576565016092841,0.0257905498141367,0.02680367986684945,0.02794499448332949,0.029609489148854085,0.0327832628041107,0.034976763665856836,0.03467807046882945,0.03352374086770249,0.030783936947649082,0.025583962929086296,0.02055904954501639,0.01814546217032173,0.017310430672934862,0.01646039541009811,0.015240828018564988,0.013862772595190684,0.01244552680994723,0.011115545448797995,0.009628640255708814,0.008856604122043922,0.009101009430225347,0.009242093728086959,0.009352901688879499,0.00945094240817701,0.009635934578021081,0.010138772126754889,0.011330813387091673,0.011892950701332769,0.011930360036350882,0.012634056181142841,0.0132915852455181,0.013616211070757583,0.01576294221325658,0.020740168585351354,0.009720039820643483,0.0038727848785737318,0.012255300399433983,0.012950738629212838,0.012231792951145182,0.009989204185630624],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"FAO Food Index Growth Rates in South Africa\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Growth rates\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('422a7cbf-a458-4e50-a46d-422afaf03bb1');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "np.log(food).diff().iplot(xTitle=\"Year\",yTitle=\"Growth rates\", title=\"FAO Food Index Growth Rates in South Africa\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Livestock index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.3214064039476915,
          0.2793761695045083,
          0.3638541182252318,
          0.3724577871640062,
          0.374072252290244,
          0.3582373809785006,
          0.4297588172888403,
          0.4663301835677832,
          0.47101039887742074,
          0.5280714801909665,
          0.5947636317634694,
          0.6840377253178039,
          0.7342119994289845,
          0.7760747262491571,
          0.5104394486662016,
          0.5859142605071445,
          0.5679351605159675,
          0.6349964695161853,
          0.6724183596571994,
          0.7320756387527486,
          0.7561875133455939,
          0.5737055069991834,
          0.4857598880347002,
          0.516665681806063,
          0.5895628070626359,
          0.633799068512631,
          0.713532317209219,
          0.7376003806029445,
          0.8562296342437888,
          0.8546696266380122,
          0.5902591123585555,
          0.584239095848148,
          0.6085193929548838,
          0.6351303473947882,
          0.6184443380967181,
          0.6260315368352113,
          0.5149182624474377,
          0.5845043891463659,
          0.7820293204320061,
          1,
          0.868242353119005,
          0.8683063948135208,
          0.9236381084360311,
          0.8312996501676201,
          0.8321894048541374,
          0.8229365203165228,
          0.8494511028177696,
          0.8757520201086328,
          0.8957825020305495,
          0.913564684059002,
          0.9301782553373922,
          0.9607747187237584,
          0.9736089313113584,
          0.9666683227383985,
          0.9305787615778185,
          0.9575141266761693,
          1.0149050602143237,
          0.9757971936171286,
          0.9862927612538005,
          1.0051710322532583,
          1.0345133984179842
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Food index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.2770115886396294,
          0.24511269603281002,
          0.3092370880306792,
          0.3200777856343457,
          0.32147908338420544,
          0.31012270794792024,
          0.37161579528484145,
          0.40426023464952326,
          0.4053956148121045,
          0.4560722702125929,
          0.510342012059571,
          0.5874490603488114,
          0.6249991556483173,
          0.658183207689808,
          0.4502799778904089,
          0.5093771157988954,
          0.49700188648836574,
          0.552068381227316,
          0.5853959203246412,
          0.6354797668879462,
          0.6576187954651107,
          0.5180170028526582,
          0.45523094748545656,
          0.4866911871870492,
          0.5424544243445777,
          0.5836605162783323,
          0.6510704446717303,
          0.6783003456836744,
          0.7847896507773241,
          0.7931561358928135,
          0.5918553398502787,
          0.5515450715429825,
          0.5939226699062614,
          0.6386766954380427,
          0.6186326290439077,
          0.6434886356854275,
          0.6011510429094223,
          0.651555637703098,
          0.7931061194265321,
          1,
          0.914770807088544,
          0.9115763847144445,
          0.9726001667491221,
          0.9326476664748601,
          0.9508896277636348,
          0.9899336788123498,
          0.9926411041750214,
          1.0123857351649501,
          1.035153426406758,
          1.0738280742367214,
          1.0999491831958397,
          1.1590640165652712,
          1.1397833211832553,
          1.1806644378860403,
          1.170708754675753,
          1.167674248162424,
          1.2752603784778354,
          1.265800393793578,
          1.225740527899391,
          1.3272182499557663,
          1.3729045426359818
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Crop index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.12405393789539884,
          0.1344313035845859,
          0.13876659267732167,
          0.1500386741108956,
          0.1584826132188729,
          0.16584300935263077,
          0.17369740175785028,
          0.1815372546018717,
          0.19012904423479446,
          0.1976901192319616,
          0.20743688210908495,
          0.21676229889485557,
          0.22922288655344703,
          0.23871255368559174,
          0.2527635596176807,
          0.26178891339296767,
          0.2760554990523474,
          0.28403763145088373,
          0.2942731491531843,
          0.3032005976991804,
          0.31526961508503165,
          0.32687462440598863,
          0.346143537949709,
          0.3681184945579946,
          0.35651380696328416,
          0.39222348375953187,
          0.40299489333261296,
          0.4405878824599237,
          0.4936798251478406,
          0.537443778749286,
          0.5701026358947022,
          0.41743967248601493,
          0.5251249361117662,
          0.6450040455654263,
          0.6139456238921559,
          0.6995247321704965,
          0.9154586954028242,
          0.8963390972153042,
          0.8421487190741248,
          1,
          1.082122641636646,
          1.0596766471150156,
          1.1383702916787992,
          1.3462983403441084,
          1.3515560621027933,
          1.5665878075081892,
          1.474428797973535,
          1.4667442318321746,
          1.495503108995923,
          1.6035465666262259,
          1.652943702636922,
          1.8113911698836298,
          1.6843039890547353,
          1.8942612589828904,
          1.9771727411781093,
          1.8697797466879233,
          2.1473795453906277,
          2.244453636470657,
          2.024802308830567,
          2.4107727436511674,
          2.5069655683513288
         ]
        },
        {
         "line": {
          "color": "rgba(128, 0, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Population",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          0.3306087873342418,
          0.3374163959803006,
          0.3448649664869298,
          0.3529435046541197,
          0.3616470630918659,
          0.37095420311014926,
          0.38098366206907547,
          0.39162824651854916,
          0.4028720148685561,
          0.41473805493911686,
          0.42712192183013853,
          0.44010332349169196,
          0.45346567418358447,
          0.46730352402590014,
          0.48186039454885576,
          0.49575046684121793,
          0.5090913788430913,
          0.5178394637908771,
          0.5262560736083679,
          0.5365136622174972,
          0.5427803562230745,
          0.5527443996919426,
          0.5678971558554284,
          0.5837892719695724,
          0.6010039903448936,
          0.6200668337418594,
          0.6406485258701772,
          0.6640216453809793,
          0.7080649603301779,
          0.7525590374797776,
          0.7781788217625791,
          0.8035039614851185,
          0.829970848878674,
          0.8566950005524585,
          0.8824879434854143,
          0.9070577816672815,
          0.9307920606484049,
          0.954270724479301,
          0.9775366505400076,
          1,
          1.0204827443282296,
          1.0381410786739456,
          1.052928277687106,
          1.0661108732088387,
          1.0790065201103158,
          1.0920307991519074,
          1.1057372683041062,
          1.1206124209173451,
          1.1367557545017126,
          1.1539902624370513,
          1.1721686224432302,
          1.1914799347604172,
          1.2118411931785387,
          1.23300008080737,
          1.2548252169567944,
          1.277169829056681,
          1.299807986296829,
          1.3224263539769594,
          1.3449446744370008,
          1.368282062797771,
          1.3908493074478558
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "FAO Food Index in Namibia"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Index"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"2e7bee3f-cef2-4806-aae3-141120a2cd28\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"2e7bee3f-cef2-4806-aae3-141120a2cd28\")) {                    Plotly.newPlot(                        \"2e7bee3f-cef2-4806-aae3-141120a2cd28\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Livestock index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.3214064039476915,0.2793761695045083,0.3638541182252318,0.3724577871640062,0.374072252290244,0.3582373809785006,0.4297588172888403,0.4663301835677832,0.47101039887742074,0.5280714801909665,0.5947636317634694,0.6840377253178039,0.7342119994289845,0.7760747262491571,0.5104394486662016,0.5859142605071445,0.5679351605159675,0.6349964695161853,0.6724183596571994,0.7320756387527486,0.7561875133455939,0.5737055069991834,0.4857598880347002,0.516665681806063,0.5895628070626359,0.633799068512631,0.713532317209219,0.7376003806029445,0.8562296342437888,0.8546696266380122,0.5902591123585555,0.584239095848148,0.6085193929548838,0.6351303473947882,0.6184443380967181,0.6260315368352113,0.5149182624474377,0.5845043891463659,0.7820293204320061,1.0,0.868242353119005,0.8683063948135208,0.9236381084360311,0.8312996501676201,0.8321894048541374,0.8229365203165228,0.8494511028177696,0.8757520201086328,0.8957825020305495,0.913564684059002,0.9301782553373922,0.9607747187237584,0.9736089313113584,0.9666683227383985,0.9305787615778185,0.9575141266761693,1.0149050602143237,0.9757971936171286,0.9862927612538005,1.0051710322532583,1.0345133984179842],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Food index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.2770115886396294,0.24511269603281002,0.3092370880306792,0.3200777856343457,0.32147908338420544,0.31012270794792024,0.37161579528484145,0.40426023464952326,0.4053956148121045,0.4560722702125929,0.510342012059571,0.5874490603488114,0.6249991556483173,0.658183207689808,0.4502799778904089,0.5093771157988954,0.49700188648836574,0.552068381227316,0.5853959203246412,0.6354797668879462,0.6576187954651107,0.5180170028526582,0.45523094748545656,0.4866911871870492,0.5424544243445777,0.5836605162783323,0.6510704446717303,0.6783003456836744,0.7847896507773241,0.7931561358928135,0.5918553398502787,0.5515450715429825,0.5939226699062614,0.6386766954380427,0.6186326290439077,0.6434886356854275,0.6011510429094223,0.651555637703098,0.7931061194265321,1.0,0.914770807088544,0.9115763847144445,0.9726001667491221,0.9326476664748601,0.9508896277636348,0.9899336788123498,0.9926411041750214,1.0123857351649501,1.035153426406758,1.0738280742367214,1.0999491831958397,1.1590640165652712,1.1397833211832553,1.1806644378860403,1.170708754675753,1.167674248162424,1.2752603784778354,1.265800393793578,1.225740527899391,1.3272182499557663,1.3729045426359818],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Crop index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.12405393789539884,0.1344313035845859,0.13876659267732167,0.1500386741108956,0.1584826132188729,0.16584300935263077,0.17369740175785028,0.1815372546018717,0.19012904423479446,0.1976901192319616,0.20743688210908495,0.21676229889485557,0.22922288655344703,0.23871255368559174,0.2527635596176807,0.26178891339296767,0.2760554990523474,0.28403763145088373,0.2942731491531843,0.3032005976991804,0.31526961508503165,0.32687462440598863,0.346143537949709,0.3681184945579946,0.35651380696328416,0.39222348375953187,0.40299489333261296,0.4405878824599237,0.4936798251478406,0.537443778749286,0.5701026358947022,0.41743967248601493,0.5251249361117662,0.6450040455654263,0.6139456238921559,0.6995247321704965,0.9154586954028242,0.8963390972153042,0.8421487190741248,1.0,1.082122641636646,1.0596766471150156,1.1383702916787992,1.3462983403441084,1.3515560621027933,1.5665878075081892,1.474428797973535,1.4667442318321746,1.495503108995923,1.6035465666262259,1.652943702636922,1.8113911698836298,1.6843039890547353,1.8942612589828904,1.9771727411781093,1.8697797466879233,2.1473795453906277,2.244453636470657,2.024802308830567,2.4107727436511674,2.5069655683513288],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(128, 0, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Population\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[0.3306087873342418,0.3374163959803006,0.3448649664869298,0.3529435046541197,0.3616470630918659,0.37095420311014926,0.38098366206907547,0.39162824651854916,0.4028720148685561,0.41473805493911686,0.42712192183013853,0.44010332349169196,0.45346567418358447,0.46730352402590014,0.48186039454885576,0.49575046684121793,0.5090913788430913,0.5178394637908771,0.5262560736083679,0.5365136622174972,0.5427803562230745,0.5527443996919426,0.5678971558554284,0.5837892719695724,0.6010039903448936,0.6200668337418594,0.6406485258701772,0.6640216453809793,0.7080649603301779,0.7525590374797776,0.7781788217625791,0.8035039614851185,0.829970848878674,0.8566950005524585,0.8824879434854143,0.9070577816672815,0.9307920606484049,0.954270724479301,0.9775366505400076,1.0,1.0204827443282296,1.0381410786739456,1.052928277687106,1.0661108732088387,1.0790065201103158,1.0920307991519074,1.1057372683041062,1.1206124209173451,1.1367557545017126,1.1539902624370513,1.1721686224432302,1.1914799347604172,1.2118411931785387,1.23300008080737,1.2548252169567944,1.277169829056681,1.299807986296829,1.3224263539769594,1.3449446744370008,1.368282062797771,1.3908493074478558],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"FAO Food Index in Namibia\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Index\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('2e7bee3f-cef2-4806-aae3-141120a2cd28');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "vars = {\"AG.PRD.LVSK.XD\":\"Livestock index\",\n",
    "        \"AG.PRD.FOOD.XD\":\"Food index\",\n",
    "        \"AG.PRD.CROP.XD\":\"Crop index\",\n",
    "        \"SP.POP.TOTL\":\"Population\"}\n",
    "\n",
    "use=[\"NAM\"]\n",
    "\n",
    "food = fix_date_index(wbdata.get_dataframe(vars, country = use)).dropna()\n",
    "# Add population back...\n",
    "Population = food.Population\n",
    "\n",
    "# Weight indices by population\n",
    "food = food.filter(regex='index$').multiply(Population,axis=0)\n",
    "\n",
    "food['Population'] = Population\n",
    "\n",
    "# No \"WLD\" or other regions; add up all countries\n",
    "food = food.groupby('date').sum().replace(0,np.nan).dropna()\n",
    "\n",
    "food.sort_index(inplace=True)\n",
    "\n",
    "# Normalize so 2000 = 1\n",
    "food = food/food.loc[2000,:]\n",
    "\n",
    "food.iplot(xTitle=\"Year\",yTitle=\"Index\", title=\"FAO Food Index in Namibia\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Livestock index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          -0.14014722676389013,
          0.26419386169386616,
          0.023370695149596,
          0.004325258349548999,
          -0.04325312467566911,
          0.1820283192816975,
          0.08166977034843592,
          0.009986240416268166,
          0.1143514816241833,
          0.11893241538467247,
          0.13984900099746195,
          0.07078474439676646,
          0.055450997788029144,
          -0.4189767935094267,
          0.13790144699407036,
          -0.031166207560561654,
          0.11161218087630354,
          0.05726126676716453,
          0.08500313442503521,
          0.03240553869781676,
          -0.2761731682962873,
          -0.1664017663818501,
          0.061681570789468454,
          0.13198524217973928,
          0.07235072032784579,
          0.11849575223822967,
          0.033174458436706744,
          0.14913641622472568,
          -0.0018236117973392807,
          -0.3701533786910689,
          -0.010251304238973025,
          0.040718472276734974,
          0.04280146729708478,
          -0.026623056525667932,
          0.012193555372591425,
          -0.19539257378907238,
          0.12675611574328804,
          0.29112794388462115,
          0.24586304498113876,
          -0.14128439463082337,
          0.00007375743942814039,
          0.06177569559633436,
          -0.10533001767579284,
          0.0010697452666501295,
          -0.01118099933338182,
          0.031711313855258216,
          0.030492589293519057,
          0.022614671445209455,
          0.019656542113734354,
          0.01802205783401825,
          0.03236371749782461,
          0.013269757438660518,
          -0.007154274640134246,
          -0.03804872362156708,
          0.02853375779368439,
          0.0582098757116389,
          -0.0392955789704237,
          0.010698457242506077,
          0.018959758722018712,
          0.028773461329419023
         ]
        },
        {
         "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Food index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          -0.12234125296438259,
          0.232390169280823,
          0.03445578848910302,
          0.004368435741147758,
          -0.035964430854665164,
          0.1808924609365784,
          0.08419830357580205,
          0.0028046012575781987,
          0.11778786724655588,
          0.11242982857529682,
          0.1407084236296785,
          0.06196076230290409,
          0.05173302493729015,
          -0.3796137613253571,
          0.12331907531739372,
          -0.024594815861459618,
          0.10507809579905036,
          0.05861648755491,
          0.08209184682882231,
          0.034245173221733316,
          -0.23861735948451307,
          -0.12920319869218,
          0.06682494232744585,
          0.1084742620648671,
          0.07321543459999302,
          0.10929834023471707,
          0.04097233128881994,
          0.14582554349695293,
          0.010604373849686294,
          -0.2927578482683477,
          -0.07053868593581203,
          0.07402556481799416,
          0.07264924686377638,
          -0.03188676695327414,
          0.039392761262427356,
          -0.06805814444109215,
          0.080516570032726,
          0.19659424058235825,
          0.231798246090412,
          -0.08908172913922269,
          -0.003498158122374126,
          0.06479767769589388,
          -0.04194557496634843,
          0.019370502225994575,
          0.04023995310991495,
          0.002731223123511166,
          0.019695765544604223,
          0.022239994333343442,
          0.036680249613131696,
          0.02403407822406632,
          0.05234881549972514,
          -0.01677462193875906,
          0.0352391877566427,
          -0.008468024329856244,
          -0.0025953902444793564,
          0.08813642778884803,
          -0.007445731713090209,
          -0.03215947053804516,
          0.07954003659619391,
          0.033843389184935624
         ]
        },
        {
         "line": {
          "color": "rgba(50, 171, 96, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Crop index",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          0.08033686048992594,
          0.03174001779550317,
          0.0780997559302683,
          0.054751803249878606,
          0.04539672256309646,
          0.04627310083558056,
          0.044146177237489814,
          0.046242129648635055,
          0.038997728528443076,
          0.04812636045744423,
          0.043974245565985726,
          0.05589347757112306,
          0.040565289929819004,
          0.05719438094260565,
          0.035084000158115414,
          0.05306342406689657,
          0.02850480546635903,
          0.03540168027255697,
          0.029886210305156924,
          0.039033568569440735,
          0.03614849213467086,
          0.05727685282331674,
          0.06155134382375815,
          -0.032031914106657955,
          0.09545882065585864,
          0.027092101265137725,
          0.08918604139429132,
          0.11377724820212476,
          0.08493697702377256,
          0.05899225073701375,
          -0.31167637078164423,
          0.22949617101591024,
          0.20562038114392955,
          -0.04935022518135446,
          0.13049478661837288,
          0.26902409570701447,
          -0.0211064480228334,
          -0.062362173467195706,
          0.1717986543575715,
          0.07892452116978894,
          -0.02096070947449035,
          0.07163385920006046,
          0.16776118535354123,
          0.0038977110182495944,
          0.1476433158808021,
          -0.060629223970149804,
          -0.005225522979957653,
          0.01941754178851085,
          0.0697551023580924,
          0.030339980223550722,
          0.09153739163202179,
          -0.07274273660519248,
          0.117476509985042,
          0.042838990197827775,
          -0.05584727436793513,
          0.13842764127201246,
          0.04421383983800187,
          -0.10299005199578681,
          0.1744752661035448,
          0.03912574825060844
         ]
        },
        {
         "line": {
          "color": "rgba(128, 0, 128, 1.0)",
          "dash": "solid",
          "shape": "linear",
          "width": 1.3
         },
         "mode": "lines",
         "name": "Population",
         "text": "",
         "type": "scatter",
         "x": [
          1961,
          1962,
          1963,
          1964,
          1965,
          1966,
          1967,
          1968,
          1969,
          1970,
          1971,
          1972,
          1973,
          1974,
          1975,
          1976,
          1977,
          1978,
          1979,
          1980,
          1981,
          1982,
          1983,
          1984,
          1985,
          1986,
          1987,
          1988,
          1989,
          1990,
          1991,
          1992,
          1993,
          1994,
          1995,
          1996,
          1997,
          1998,
          1999,
          2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          "",
          0.020381999020012698,
          0.021835174914565103,
          0.023155061725579795,
          0.02436077175253737,
          0.02540984083149367,
          0.026677879262535065,
          0.02755654660463447,
          0.028305891432416797,
          0.029028197490952645,
          0.02942237566367245,
          0.029940021771984182,
          0.029910050342890182,
          0.030059415122122624,
          0.03067544330454397,
          0.02841827485422721,
          0.026554817565709654,
          0.017037752112189497,
          0.016122647464417605,
          0.019304100974620098,
          0.011612710388371972,
          0.018190950374997406,
          0.027044650725801755,
          0.027599743350488648,
          0.029061491979308407,
          0.03122569456522467,
          0.03265371637466846,
          0.035833762448412076,
          0.06422109395311015,
          0.06094360730466081,
          0.03347689712304547,
          0.03202576966054646,
          0.03240846288912613,
          0.031691384908123676,
          0.02966316369216887,
          0.02746102750337992,
          0.02582974734724347,
          0.024911507679185332,
          0.02408837584417201,
          0.022719493666929057,
          0.020275794088281365,
          0.01715589536402311,
          0.014143429021858021,
          0.012442210499652308,
          0.01202340001823124,
          0.011998352284495542,
          0.012473242341721133,
          0.01336301663618139,
          0.014303035696071068,
          0.015047354003648955,
          0.01562982665632967,
          0.016340620485790658,
          0.01694467323524554,
          0.017309439387877046,
          0.01754600380832677,
          0.01765026532755809,
          0.017569991854466116,
          0.017251645516038527,
          0.01688468173438651,
          0.017203106242391575,
          0.016358588900273308
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         },
         "text": "FAO Food Index Growth Rates in Namibia"
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Year"
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": "Growth rates"
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"cc485914-1eb5-4148-84cc-2a1305b7f348\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"cc485914-1eb5-4148-84cc-2a1305b7f348\")) {                    Plotly.newPlot(                        \"cc485914-1eb5-4148-84cc-2a1305b7f348\",                        [{\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Livestock index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",-0.14014722676389013,0.26419386169386616,0.023370695149596,0.004325258349548999,-0.04325312467566911,0.1820283192816975,0.08166977034843592,0.009986240416268166,0.1143514816241833,0.11893241538467247,0.13984900099746195,0.07078474439676646,0.055450997788029144,-0.4189767935094267,0.13790144699407036,-0.031166207560561654,0.11161218087630354,0.05726126676716453,0.08500313442503521,0.03240553869781676,-0.2761731682962873,-0.1664017663818501,0.061681570789468454,0.13198524217973928,0.07235072032784579,0.11849575223822967,0.033174458436706744,0.14913641622472568,-0.0018236117973392807,-0.3701533786910689,-0.010251304238973025,0.040718472276734974,0.04280146729708478,-0.026623056525667932,0.012193555372591425,-0.19539257378907238,0.12675611574328804,0.29112794388462115,0.24586304498113876,-0.14128439463082337,0.00007375743942814039,0.06177569559633436,-0.10533001767579284,0.0010697452666501295,-0.01118099933338182,0.031711313855258216,0.030492589293519057,0.022614671445209455,0.019656542113734354,0.01802205783401825,0.03236371749782461,0.013269757438660518,-0.007154274640134246,-0.03804872362156708,0.02853375779368439,0.0582098757116389,-0.0392955789704237,0.010698457242506077,0.018959758722018712,0.028773461329419023],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(55, 128, 191, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Food index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",-0.12234125296438259,0.232390169280823,0.03445578848910302,0.004368435741147758,-0.035964430854665164,0.1808924609365784,0.08419830357580205,0.0028046012575781987,0.11778786724655588,0.11242982857529682,0.1407084236296785,0.06196076230290409,0.05173302493729015,-0.3796137613253571,0.12331907531739372,-0.024594815861459618,0.10507809579905036,0.05861648755491,0.08209184682882231,0.034245173221733316,-0.23861735948451307,-0.12920319869218,0.06682494232744585,0.1084742620648671,0.07321543459999302,0.10929834023471707,0.04097233128881994,0.14582554349695293,0.010604373849686294,-0.2927578482683477,-0.07053868593581203,0.07402556481799416,0.07264924686377638,-0.03188676695327414,0.039392761262427356,-0.06805814444109215,0.080516570032726,0.19659424058235825,0.231798246090412,-0.08908172913922269,-0.003498158122374126,0.06479767769589388,-0.04194557496634843,0.019370502225994575,0.04023995310991495,0.002731223123511166,0.019695765544604223,0.022239994333343442,0.036680249613131696,0.02403407822406632,0.05234881549972514,-0.01677462193875906,0.0352391877566427,-0.008468024329856244,-0.0025953902444793564,0.08813642778884803,-0.007445731713090209,-0.03215947053804516,0.07954003659619391,0.033843389184935624],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(50, 171, 96, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Crop index\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",0.08033686048992594,0.03174001779550317,0.0780997559302683,0.054751803249878606,0.04539672256309646,0.04627310083558056,0.044146177237489814,0.046242129648635055,0.038997728528443076,0.04812636045744423,0.043974245565985726,0.05589347757112306,0.040565289929819004,0.05719438094260565,0.035084000158115414,0.05306342406689657,0.02850480546635903,0.03540168027255697,0.029886210305156924,0.039033568569440735,0.03614849213467086,0.05727685282331674,0.06155134382375815,-0.032031914106657955,0.09545882065585864,0.027092101265137725,0.08918604139429132,0.11377724820212476,0.08493697702377256,0.05899225073701375,-0.31167637078164423,0.22949617101591024,0.20562038114392955,-0.04935022518135446,0.13049478661837288,0.26902409570701447,-0.0211064480228334,-0.062362173467195706,0.1717986543575715,0.07892452116978894,-0.02096070947449035,0.07163385920006046,0.16776118535354123,0.0038977110182495944,0.1476433158808021,-0.060629223970149804,-0.005225522979957653,0.01941754178851085,0.0697551023580924,0.030339980223550722,0.09153739163202179,-0.07274273660519248,0.117476509985042,0.042838990197827775,-0.05584727436793513,0.13842764127201246,0.04421383983800187,-0.10299005199578681,0.1744752661035448,0.03912574825060844],\"type\":\"scatter\"},{\"line\":{\"color\":\"rgba(128, 0, 128, 1.0)\",\"dash\":\"solid\",\"shape\":\"linear\",\"width\":1.3},\"mode\":\"lines\",\"name\":\"Population\",\"text\":\"\",\"x\":[1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],\"y\":[\"\",0.020381999020012698,0.021835174914565103,0.023155061725579795,0.02436077175253737,0.02540984083149367,0.026677879262535065,0.02755654660463447,0.028305891432416797,0.029028197490952645,0.02942237566367245,0.029940021771984182,0.029910050342890182,0.030059415122122624,0.03067544330454397,0.02841827485422721,0.026554817565709654,0.017037752112189497,0.016122647464417605,0.019304100974620098,0.011612710388371972,0.018190950374997406,0.027044650725801755,0.027599743350488648,0.029061491979308407,0.03122569456522467,0.03265371637466846,0.035833762448412076,0.06422109395311015,0.06094360730466081,0.03347689712304547,0.03202576966054646,0.03240846288912613,0.031691384908123676,0.02966316369216887,0.02746102750337992,0.02582974734724347,0.024911507679185332,0.02408837584417201,0.022719493666929057,0.020275794088281365,0.01715589536402311,0.014143429021858021,0.012442210499652308,0.01202340001823124,0.011998352284495542,0.012473242341721133,0.01336301663618139,0.014303035696071068,0.015047354003648955,0.01562982665632967,0.016340620485790658,0.01694467323524554,0.017309439387877046,0.01754600380832677,0.01765026532755809,0.017569991854466116,0.017251645516038527,0.01688468173438651,0.017203106242391575,0.016358588900273308],\"type\":\"scatter\"}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"FAO Food Index Growth Rates in Namibia\"},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Year\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"Growth rates\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('cc485914-1eb5-4148-84cc-2a1305b7f348');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "np.log(food).diff().iplot(xTitle=\"Year\",yTitle=\"Growth rates\", title=\"FAO Food Index Growth Rates in Namibia\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
