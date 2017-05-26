!conda create -n tf_env --copy -y -q python=2
!conda install -n tf_env -y python=2.7.11
!bash ./pip-install-pydoop.sh
!conda install -n tf_env -y -c conda-forge tensorflow
