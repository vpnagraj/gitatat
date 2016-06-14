# -*- coding: utf-8 -*-

import argparse
import os

def main():
    
    parser =  argparse.ArgumentParser(prog='gitatat')
    
    parser.add_argument('input_file', default='.', nargs='?', help='file to be added')
        
    args = parser.parse_args()
    
    gitadd = "git add " + args.input_file

    commitmessage = raw_input("commit message: ")

    gitcommit = "git commit -m " + commitmessage

    gitpush = "git push origin master"

    os.system(gitadd + " ; " + gitcommit + " ; " + gitpush)
    
    # TODO: include workflow for updating gh-pages 
    # git branch -v | grep -c "gh-pages"
    # git checkout gh-pages
    # git rebase master
    # git push origin gh-pages
    # git checkout master
        
if __name__ == '__main__':
    main()