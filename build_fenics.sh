sudo -H pip3 install ply
sudo apt-get install libeigen3-dev

sudo apt-get install libpetsc3.7.3-dev 
sudo apt-get install slepc-dev 
#sudo -H pip3 search python-vtk

wget http://www.vtk.org/files/release/7.1/VTK-7.1.1.zip
unzip VTK-7.1.1.zip
cd ../VTK-7.1.1/
cd ../build/
cmake ..
make -j12
sudo make install
cd ../..

git clone https://bitbucket.org/slepc/slepc
cd slepc/
git co v3.7
sudo -H pip3 install .
cd ..

git clone https://bitbucket.org/slepc/slepc4py
cd slepc4py/
git co 3.7.0 
sudo -H pip3 install .
cd ..

sudo apt-get install scotch

sudo apt-get install python-petsc4py 
sudo -H pip3 install petsc4py


git clone https://bitbucket.org/fenics-project/fiat.git
cd fiat/
sudo -H pip3 . install
cd ..

git clone https://bitbucket.org/fenics-project/instant.git
cd ../instant/
sudo -H pip3 install .
cd ..

git clone https://bitbucket.org/fenics-project/dijitso.git
cd ../dijitso/
sudo -H pip3 install .
cd ..

git clone https://bitbucket.org/fenics-project/ufl.git
cd ../ufl/
sudo -H pip3 install .
cd ..

git clone https://bitbucket.org/fenics-project/ffc.git
cd ../ffc/
sudo -H pip3 install .
cd ..

git clone https://bitbucket.org/fenics-project/dolfin.git
cd ../dolfin/
mkdir build
cd build
cmake ..
make -j12
sudo make install

git clone https://bitbucket.org/fenics-project/mshr.git
cd ../../mshr/
mkdir build 
cd build/
cmake ..
make -j12
sudo make install

