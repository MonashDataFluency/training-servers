
FROM rocker/tidyverse

ENV ROOT TRUE


#RUN Rscript -e 'install.packages("glmnet")'

COPY 02-setup /etc/cont-init.d
COPY create-users /home/rstudio
COPY share /home/rstudio

