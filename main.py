import os
import sys
import shutil
import string

SANDBOX_DIR = "sandbox"

VAGRANT_CONFIG_TEMPLATE = open("vagrant_template.recipe").read()
BOOTSTRAP = open("bootstrap.recipe").read()
LINUX_PIP_INSTALL = open("linux_pip.recipe").read()
LINUX_TAR32_INSTALL = open("linux_tar32.recipe").read()
LINUX_TAR64_INSTALL = open("linux_tar64.recipe").read()
OSX_PIP_INSTALL = open("osx_pip.recipe").read()
OSX_TAR_INSTALL = open("osx_tar.recipe").read()
WINDOWS_ZIP_INSTALL = open("windows_zip.recipe").read()

BOXES_LINUX32 = ["debian-7.1.0-i386",
                 "ubuntu-12.04-i386",
                 "ubuntu-14.04-i386",
                ]

BOXES_LINUX64 = ["debian-7.1.0-amd64",
                 "ubuntu-12.04-amd64",
                 "ubuntu-14.04-amd64",
                ]


def writeToFile(file, contents):
  with open(os.path.join(SANDBOX_DIR,file),"w") as fh:
    fh.write(contents)


def resetSandbox():
  if os.path.exists(SANDBOX_DIR):
    shutil.rmtree(SANDBOX_DIR)
  os.mkdir(SANDBOX_DIR)


def doInstallWithVagrant(boxName, installName, installScript):
  vagrant_config = string.replace(VAGRANT_CONFIG_TEMPLATE, "BOX_NAME", boxName)

  writeToFile("Vagrantfile", vagrant_config)
  writeToFile("bootstrap.sh", BOOTSTRAP)
  writeToFile("install_fteproxy.sh", installScript)

  os.system("chmod 755 "+SANDBOX_DIR+"/*.sh")
  os.system("cd " + SANDBOX_DIR + " && vagrant up 2> " + boxName + "." + installName + ".err.log > " + boxName + "." + installName + ".log")

  if os.path.exists(os.path.join(SANDBOX_DIR, "success")):
    print boxName + "\t" + installName + "\t\t" + "SUCCESS"
  else:
    print boxName + "\t" + installName + "\t\t" + "FAIL"


def doInstallWithoutVagrant(boxName, installName, installScript):
  writeToFile("install_fteproxy.sh", installScript)

  os.system("chmod 755 "+SANDBOX_DIR+"/*.sh")
  os.system("cd " + SANDBOX_DIR + " && ./install_fteproxy.sh 2> " + boxName + "." + installName + ".err.log > " + boxName + "." + installName + ".log")

  if os.path.exists(os.path.join(SANDBOX_DIR, "success")):
    print boxName + "\t" + installName + "\t\t" + "SUCCESS"
  else:
    print boxName + "\t" + installName + "\t\t" + "FAIL"


def main():
  print "config\t\tinstall_method\tresult"

  # # Linux 32-bit
  # for boxName in BOXES_LINUX32:
  #   resetSandbox()
  #   doInstallWithVagrant(boxName, "pip", LINUX_PIP_INSTALL)
  #   resetSandbox()
  #   doInstallWithVagrant(boxName, "tar", LINUX_TAR32_INSTALL)
  #
  # # Linux 64-bit
  # for boxName in BOXES_LINUX64:
  #   resetSandbox()
  #   doInstallWithVagrant(boxName, "pip", LINUX_PIP_INSTALL)
  #   resetSandbox()
  #   doInstallWithVagrant(boxName, "tar", LINUX_TAR64_INSTALL)
  #
  # # OSX
  # resetSandbox()
  # doInstallWithoutVagrant("osx-10.9", "pip", OSX_PIP_INSTALL)
  # resetSandbox()
  # doInstallWithoutVagrant("osx-10.9", "tar", OSX_TAR_INSTALL)

  # Windows
  resetSandbox()
  doInstallWithVagrant("windows-7", "zip", WINDOWS_ZIP_INSTALL)
  VAGRANT_DEFAULT_PROVIDER=parallels

if __name__ == "__main__":
  main()
