import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
  'httpd',
  'firewalld'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


@pytest.mark.parametrize('svc', [
  'httpd',
  'firewalld'
])
def test_service(host, svc):
  # Note the different ways to make assertion
  assert host.service(svc).is_enabled

def test_file_contents(host):
  contents = host.file("/tmp/demo.txt").content.decode("utf-8")
  assert "Demo File Content" in contents
