# Budgetlake

## Installing/Updating Cygwin64
- They both use the same executable available at https://www.cygwin.com/install.html
- Click the hyperlink `setup-x86_64.exe` for a 64b machine (`https://www.cygwin.com/setup-x86_64.exe`)
- You DO NOT need to add `C:\cygwin64\bin` to the path.  If you get an error about a `cygwin1.dll` not being found, try uninstalling and reinstalling with this guide.

1. Make sure to point it at `C:\cygwin64`
2. Pick a mirror site in the US from `https://cygwin.com/mirrors.html` (I had success with `http://cygwin.mirror.constant.com/` in New Jersey)
3. Install the latest (or latest verified) version of three packages:
    1. `gcc-core` (`gcc-core-11.2.0-1` verified)
    2. `pkg-config (pkg-config-1.6.3-1` verified)
    3. `libusb1.0` (NOT THE DEVEL OR SRC VERSION, JUST `libusb1.0`) (`libusb1.0-1.0.21-1` verified)
4. Finish running setup executable and (unless it works after a couple tries) continue past download errors (have been able to successfully ignore `man-db-2.7.6.1-1` failing)
5. Ensure you have an SSH key for gitlab.com (sign in with your github.com account so you don't have to make another)
6. `git clone git@gitlab.com:DavidGriffith/minipro.git`
    - `https://gitlab.com/DavidGriffith/minipro`
    - Do this in Git Bash; Cygwin terminal DOES NOT WORK (probably doesn't have same .ssh key lookup process as Git Bash?)
7. In Cygwin terminal:
    ```
    cd minipro
    make
    ```
8. Done.  You can now call minipro.exe from your Makefile in Git Bash on Windows.
