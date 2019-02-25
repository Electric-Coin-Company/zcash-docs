:orphan:

.. _development_guidelines:

Development Guidelines
======================

We achieve our design goals primarily through this codebase as a
reference implementation. This repository is a fork of `Bitcoin Core <https://github.com/bitcoin/bitcoin>`_
as of upstream release 0.11.2 (many later Bitcoin PRs have also been
ported to Zcash). It implements the `Zcash protocol <https://github.com/zcash/zips/blob/master/protocol/protocol.pdf>`_ 
and a few other distinct features.

    - Bitcoin Core: https://github.com/bitcoin/bitcoin
    - Zcash Protocol: https://github.com/zcash/zips/blob/master/protocol/protocol.pdf

Zcash Github Workflow
---------------------

This document describes the standard workflows and terminology for developers at Zcash. 
It is intended to provide procedures that will allow users to contribute to the 
open-source code base. Below are common workflows users will encounter:

    1. :ref:`Fork Zcash Repository`
    2. :ref:`Create Branch`
    3. :ref:`Make & Commit Changes`
    4. :ref:`Create Pull Request`
    5. :ref:`Discuss / Review PR`
    6. :ref:`Deploy / Merge PR`

Before continuing, please ensure you have an existing Github or Gitlab account. 
If not, visit `Github <https://github.com>`_ or `Gitlab <https://gitlab.com>`_ to create an account. 

.. _Fork Zcash Repository:

Fork Zcash Repository
*********************

This step assumes you are starting with a new Github/Gitlab environment. 
If you have already forked the Zcash repository, please continue to :ref:`Create Branch` 
section. Otherwise, open up a terminal and issue the below commands:

.. note:: Please replace ``your_username``, with your actual Github username

.. code-block:: bash
    
    git clone git@github.com:your_username/zcash.git
    cd zcash
    git remote set-url origin git@github.com:your_username/zcash.git
    git remote add upstream git@github.com:zcash/zcash.git
    git remote set-url --push upstream DISABLED
    git fetch upstream
    git branch -u upstream/master master

After issuing the above commands, your ``.git/config`` file should look similar to the following:

.. code-block:: bash
    
    [core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
    [remote "origin"]
        url = git@github.com:your_username/zcash.git
        fetch = +refs/heads/*:refs/remotes/origin/*
    [branch "master"]
        remote = upstream
        merge = refs/heads/master
    [remote "upstream"]
        url = git@github.com:zcash/zcash.git
        fetch = +refs/heads/*:refs/remotes/upstream/*
        pushurl = DISABLED

This setup provides a single cloned environment to develop for Zcash. There are 
alternative methods using multiple clones, but this document does not cover that process.

.. _Create Branch:

Create Branch
*************

While working on the Zcash project, you are going to have bugs, features, and ideas to work on. 
Branching exists to aid these different tasks while you write code. Below are some conventions 
of branching at Zcash:

    1. ``master`` branch is **ALWAYS** deployable
    2. Avoid branching directly off ``master``, instead use your local fork
    3. Branch names **MUST** be descriptive (e.g. ``issue#_short_description``)

To create a new branch (assuming you are in ``zcash`` directory):

.. code-block:: bash
    
    git checkout -b [new_branch_name]

.. note:: Even though you have created a new branch, until you ``git push`` this local branch, it will not show up in your Zcash fork on Github (e.g. https://github.com/your_username/zcash)

To checkout an existing branch (assuming you are in ``zcash`` directory):

.. code-block:: bash
    
    git checkout [existing_branch_name]

If you are fixing a bug or implementing a new feature, you likely will want to create a new branch. 
If you are reviewing code or working on existing branches, you likely will checkout an existing 
branch. To view the list of current Zcash Github issues, click `here <https://github.com/zcash/zcash/issues>`_ . 

.. _Make & Commit Changes:

Make & Commit Changes
*********************

If you have created a new branch or checked out an existing one, it is time to make 
changes to your local source code. Below are some formalities for commits:

    1. Commit messages **MUST** be clear
    2. Commit messages **MUST** be descriptive
    3. Commit messages **MUST** be clean (see :ref:`Squashing Commits` for details)

Commit messages should contain enough information in the first line to be able to scan a 
list of patches and identify which one is being searched for. Do not use "auto-close" 
keywords -- tickets should be closed manually. The auto-close keywords are "close[ds]", 
"resolve[ds]", and "fix(e[ds])?"

While continuing to do development on a branch, keep in mind that other approved commits 
are getting merged into ``master``.  In order to ensure there are minimal to no merge conflicts, 
we need ``rebase`` with master.

If you are new to this process, please sanity check your remotes:

.. code-block:: bash

    git remote -v

.. code-block:: bash
    
    origin    git@github.com:your_username/zcash.git (fetch)
    origin    git@github.com:your_username/zcash.git (push)
    upstream    git@github.com:zcash/zcash.git (fetch)
    upstream    DISABLED (push)

This output should be consistent with your ``.git/config``:

.. code-block:: bash

    [branch "master"]
        remote = upstream
        merge = refs/heads/master
    [remote "origin"]
        url = git@github.com:your_username/zcash.git
        fetch = +refs/heads/*:refs/remotes/origin/*
    [remote "upstream"]
        url = git@github.com:zcash/zcash.git
        fetch = +refs/heads/*:refs/remotes/upstream/*
        pushurl = DISABLED

Once you have confirmed your branch/remote is valid, issue the following commands 
(assumes you have **NO** existing uncommitted changes):

.. code-block:: bash
    
    git fetch upstream
    git rebase upstream/master
    git push -f

If you have uncommitted changes, use ``git stash`` to preserve them:

.. code-block:: bash

    git stash
    git fetch upstream
    git rebase upstream/master
    git push -f
    git stash pop

Using ``git stash`` allows you to temporarily store your changes while you rebase 
with ``master``. Without this, you will rebase with master and lose your local changes.

Before committing changes, ensure your commit messages follow these guidelines:

    1. Separate subject from body with a blank line
    2. Limit the subject line to 50 characters
    3. Capitalize the subject line
    4. Do not end the subject line with a period
    5. Wrap the body at 72 characters
    6. Use the body to explain *what* and *why* vs. *how*

Once synced with ``master``, let's commit our changes:

.. code-block:: bash

    git add [files...] # default is all files, be careful not to add unintended files
    git commit -m 'Message describing commit'
    git push

Now that all the files changed have been committed, let's continue to Create Pull Request section.

.. _Create Pull Request:

Create Pull Request
*******************

On your Github page (e.g. https://github.com/your_username/zcash), you will notice a newly created 
banner containing your recent commit with a big green ``Compare & pull request`` button. Click on it.

.. image:: images/github-cmp-pr-button.png

First, write a brief summary comment for your PR -- this first comment should be no more than a 
few lines because it ends up in the merge commit message. This comment should mention the issue 
number preceded by a hash symbol (e.g. #2984).

Add a second comment if more explanation is needed. It's important to explain why this pull request
should be accepted. State whether the proposed change fixes part of the problem or all of it; 
if the change is temporary (a workaround) or permanent; if the problem also exists upstream 
(Bitcoin) and, if so, if and how it was fixed there.

If you click on `Commits`, you should see the diff of that commit; it's advisable to verify 
it's what you expect. You can also click on the small plus signs that appear when you hover 
over the lines on either the left or right side and add a comment specific to that part of 
the code. This is very helpful, as you don't have to tell the reviewers (in a general comment)
that you're referring to a certain line in a certain file.

Add comments **before** adding reviewers, otherwise they will get a separate email for each
comment you add. Once you're happy with the documentation you've added to your PR, 
select reviewers along the right side. For a trivial change (like the example here), one 
reviewer is enough, but generally you should have at least two reviewers, at least one 
of whom should be experienced. It may be good to add one less experienced engineer as a 
learning experience for that person.

.. _Discuss / Review PR:

Discuss / Review PR
*******************

In order to merge your PR with ``master``, you will need to convince the reviewers of the intentions of your code. 

.. important:: If your PR introduces code that does not have existing tests to ensure it operates gracefully, you **MUST** also create these tests to accompany your PR.

Reviewers will investigate your PR and provide feedback. Generally the comments are explicitly 
requesting code changes or clarifying implementations. Otherwise Reviewers will reply with PR terminology:

    - **Concept ACK** - Agree with the idea and overall direction, but have neither reviewed nor tested the code changes.

    - **utACK (untested ACK)** - Reviewed and agree with the code changes but haven't actually tested them.

    - **Tested ACK** - Reviewed the code changes and have verified the functionality or bug fix.

    - **ACK** - A loose ACK can be confusing. It's best to avoid them unless it's a documentation/comment only change in which case there is nothing to test/verify; therefore the tested/untested distinction is not there.

    - **NACK** - Disagree with the code changes/concept. Should be accompanied by an explanation.

.. _Squashing Commits:

Squashing Commits
~~~~~~~~~~~~~~~~~

Before your PR is accepted, you might be requested to squash your commits to clean up the logs. This 
can be done using the following approach:

.. code-block:: bash

    git checkout branch_name
    git rebase -i HEAD~4

The integer value after `~` represents the number of commits you would like to interactively rebase. 
You can pick a value that makes sense for your situation. A template will pop-up in your terminal 
requesting you to specify what commands you would like to do with each prior commit:

.. code-block:: console
    
    Commands:
    p, pick = use commit
    r, reword = use commit, but edit the commit message
    e, edit = use commit, but stop for amending
    s, squash = use commit, but meld into previous commit
    f, fixup = like "squash", but discard this commit's log message
    x, exec = run command (the rest of the line) using shell

Modify each line with the according command, followed by the hash of the commit. For example, 
if I wanted to squash my last 4 commits into the most recent commit for this PR:

.. code-block:: bash
    
    p 1fc6c95 Final commit message
    s 6b2481b Third commit message
    s dd1475d Second commit message
    s c619268  First commit message

.. code-block:: bash
    
    git push origin branch-name --force

.. _Deploy / Merge PR:

Deploy / Merge PR
*****************

.. important:: **DO NOT** click on this button! We use a different process (``zkbot``, ``Homu``) to merge code

   .. image:: images/github-merge-button.png


.. admonition:: zkbot

   We use a homu instance called ``zkbot`` to merge *all* PRs. (Direct pushing to the ``master`` branch of the repo is not allowed.) Here's just a quick overview of how it works.

   If you're on our team, you can do ``@zkbot <command>`` to tell zkbot to do things. Here are a few examples:

      * ``r+ [commithash]`` this will test the merge and then actually commit the merge into the repo if the tests succeed.
      * ``try`` this will test the merge and nothing else.
      * ``rollup`` this is like ``r+`` but for insignificant changes. Use this when we want to test a bunch of merges at once to save Buildbot time.

   More instructions are found here: http://ci.z.cash:12477/


Once you have addressed the comments in your PR, and it has received two *ACKs* 
from reviewers, you can attempt to test merge the PR:

.. code-block:: bash
    
    @zkbot try

.. note:: ``@zkbot`` commands are entered into Github tickets as comments

This will instruct Buildbot(aka Homu) to test merging your PR with ``master`` and ensure it 
passes the full test suite. You may or may not have permissions to run this command, but 
Github will reply with output indicating if you can or not.

If the ``@zkbot try`` fails, you will need to go back and address the issues accordingly. 
Otherwise, you can now attempt to merge into ``master``:

.. code-block:: bash
    
    @zkbot r+

.. note:: ``@zkbot`` commands are entered into Github tickets as comments

There are very few people that have ``@zkbot r+`` privileges, so you can request one of these 
people to merge the PR, or leave it for the release process to pick it up. Finally, when the 
PR is merged into ``master`` successfully, your PR will close.

There will be times when your PR is waiting for some portion of the above process. If you 
are requested to rebase your PR, in order to gracefully merge into ``master``, please do the following:

.. code-block:: bash

    git checkout branch_name
    git fetch upstream
    git rebase upstream/master
    git push -f

----

Zcash Developer Workflow
------------------------

.. tip:: The flow below assumes you have already downloaded the parameters using ``./zcutil/fetch-params.sh`` 

Below describes a standard workflow for developing code in the zcash repository:

    1. Clone your zcash fork
        .. code-block:: bash

            git clone git@github.com:your_username/zcash.git

    2. Create a branch for local changes
        .. code-block:: bash

            cd zcash
            git checkout -b [new_branch_name]

    3. Build zcash
        .. code-block:: bash

            /zcutil/build.sh -j$(nproc)

    4. Create & build changes to code
        .. code-block:: bash

            make

This will allow you to create/edit existing Zcash code, and build it locally. 
If you want to submit a PR for this newly created code, please refer back to
:ref:`Make & Commit Changes` section. After completing those steps, please ensure
you have also followed :ref:`Create Pull Request` and :ref:`Deploy / Merge PR` sections.

Coding
******

See the `Developer notes <https://github.com/zcash/zcash/blob/master/doc/developer-notes.md>`_ documentation which details coding style, thread handling and additional tips.

Testing
*******

To ensure the existing Zcash code is tested, we use the following tools:

Gtest
~~~~~

Add unit tests for Zcash under ``./src/gtest``. 

To list all tests, run ``./src/zcash-gtest --gtest_list_tests``.

To run a subset of tests, use a regular expression with the flag ``--gtest_filter``. Example:

.. code-block:: bash

    ./src/zcash-gtest --gtest_filter=DeprecationTest.*

For debugging: ``--gtest_break_on_failure``.

BOOST
~~~~~

To run a subset of BOOST tests:

.. code-block:: bash
    
    src/test/test_bitcoin -t TESTGROUP/TESTNAME

RPC Tests
~~~~~~~~~

To run the main test suite:

.. code-block:: bash

    qa/zcash/full_test_suite.py

To run the RPC tests:

.. code-block:: bash

    qa/pull-tester/rpc-tests.sh

The main test suite uses two different testing frameworks. Tests using the Boost 
framework are under ``src/test/``; tests using the Google Test/Google Mock framework 
are under ``src/gtest/`` and ``src/wallet/gtest/``. The latter framework is preferred 
for new Zcash unit tests.

RPC tests are implemented in Python under the qa/rpc-tests/ directory.

Continuous Integration
----------------------

:fa:`arrow-circle-right` `Buildbot <https://ci.z.cash/>`_

:fa:`arrow-circle-right` `Homu <https://ci.z.cash/queue/zcash>`_

Release Versioning
------------------

Starting from Zcash v1.0.0-beta1, Zcash version numbers and release tags take one of the following forms:

    v<X>.<Y>.<Z>-beta<N>

    v<X>.<Y>.<Z>-rc<N>

    v<X>.<Y>.<Z>

    v<X>.<Y>.<Z>-<N>

Alpha releases used a different convention: ``v0.11.2.z<N>`` (because Zcash was forked from Bitcoin v0.11.2).

Release Process
---------------

For details on zcashd release processes, see:

- `Release Process <https://github.com/zcash/zcash/blob/master/doc/hotfix-process.md>`_
- `Hotfix Release Process <https://github.com/zcash/zcash/blob/master/doc/hotfix-process.md>`_
