#!/usr/bin/env python3

import logging

import common.blackbear_common as bb
import common.commands as commands

#----------------------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    args = commands.parseCommandLine()
    args.func(args, bb.EJ26_SeasonId, bb.League.EJ)
