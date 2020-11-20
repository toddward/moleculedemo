# moleculedemo

## Objective

Provide a quick overview of molecule usage and example tests.  Questions, contact Todd Wardzinski (todd.wardzinski@redhat.com)

## Prerequisites

* Set up environment (suggested VirtualEnv):

  ```bash
  dnf module install container-tools -y

  python3 -m pip install "molecule[ansible,lint,podman]" --user

  python3 -m pip install pytest-testinfra --user
    ```

## Generating Skeleton Framework for Molecule

* `molecule init role -d podman --verifier-name testinfra your_role_name`
* Generates the framework necessary to run the test.

## Demos

### Demo 1 - Testing For File

1. Execute `molecule test` within demo1 directory.
2. Expected results:

    ```bash
        ============================= test session starts ==============================
      platform linux -- Python 3.6.8, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
      rootdir: /home/toddwardzinski/moleculedemo/demo1/molecule/default
      plugins: testinfra-6.1.0
      collected 10 items                                                             
      
      tests/test_default.py ....F....F                                         [100%]
      
      =================================== FAILURES ===================================
      ____________________ test_file_contents[ansible://centos7] _____________________
      
      host = <testinfra.host.Host ansible://centos7>
      
          def test_file_contents(host):
      >     contents = host.file("/tmp/demo.txt").content.decode("utf-8")
      
      tests/test_default.py:28:
      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
      ../../../../.local/lib/python3.6/site-packages/testinfra/modules/file.py:143: in content
          return self._get_content(False)
      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
      
      self = <file /tmp/demo.txt>, decode = False
      
          def _get_content(self, decode):
              out = self.run_test("cat -- %s", self.path)
              if out.rc != 0:
      >           raise RuntimeError("Unexpected output %s" % (out,))
      E           RuntimeError: Unexpected output CommandResult(command='cat -- /tmp/demo.txt', exit_status=1, stdout='', stderr='cat: /tmp/demo.txt: No such file or directory')
      
      ../../../../.local/lib/python3.6/site-packages/testinfra/modules/file.py:131: RuntimeError
      ____________________ test_file_contents[ansible://centos8] _____________________
      
      host = <testinfra.host.Host ansible://centos8>
      
          def test_file_contents(host):
      >     contents = host.file("/tmp/demo.txt").content.decode("utf-8")
      
      tests/test_default.py:28:
      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
      ../../../../.local/lib/python3.6/site-packages/testinfra/modules/file.py:143: in content
          return self._get_content(False)
      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
      
      self = <file /tmp/demo.txt>, decode = False
      
          def _get_content(self, decode):
              out = self.run_test("cat -- %s", self.path)
              if out.rc != 0:
      >           raise RuntimeError("Unexpected output %s" % (out,))
      E           RuntimeError: Unexpected output CommandResult(command='cat -- /tmp/demo.txt', exit_status=1, stdout='', stderr='cat: /tmp/demo.txt: No such file or directory')
      
      ../../../../.local/lib/python3.6/site-packages/testinfra/modules/file.py:131: RuntimeError
      =========================== short test summary info ============================
      FAILED tests/test_default.py::test_file_contents[ansible://centos7] - Runtime...
      FAILED tests/test_default.py::test_file_contents[ansible://centos8] - Runtime...
      =================== 2 failed, 8 passed in 176.60s (0:02:56) ====================
    ```

3. Uncomment the last lines in `tasks/main.yml` and run your test again, `molecule test`.  Expected results:

    ```bash
    ============================= test session starts ==============================
    platform linux -- Python 3.6.8, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
    rootdir: /home/toddwardzinski/moleculedemo/demo1/molecule/default
    plugins: testinfra-6.1.0
    collected 10 items                                                             
    
    tests/test_default.py ..........                                         [100%]
    
    ======================== 10 passed in 175.42s (0:02:55) ========================
    Verifier completed successfully.
    ```

