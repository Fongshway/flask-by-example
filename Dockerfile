################################################################################
# https://github.com/Fongshway/docker-python/blob/master/Dockerfile
FROM fongshway/python:production
################################################################################
ENV PROJECT_DIR="/opt/app" \
    PYTHONPATH="${PYTHONPATH}:${PROJECT_DIR}" \
    USER=flask

# -- Create non-root user:
RUN useradd -ms /bin/bash ${USER} && \
    mkdir -p "${PROJECT_DIR}" && \
    chown -R ${USER}: "${PROJECT_DIR}" /usr/local /home/${USER} && \
    usermod -aG sudo ${USER} && \
    sed -i.bkp -e 's/%sudo\s\+ALL=(ALL\(:ALL\)\?)\s\+ALL/%sudo ALL=NOPASSWD:ALL/g' /etc/sudoers

# -- Create application directory:
RUN set -ex && mkdir -p ${PROJECT_DIR}

WORKDIR "${PROJECT_DIR}"

# -- Setup as non-root user
USER ${USER}
COPY . "${PROJECT_DIR}"
RUN sudo chown -R ${USER}: "${PROJECT_DIR}"
EXPOSE 5000

# -- Set default command
CMD flask run
