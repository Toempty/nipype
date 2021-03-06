# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import affScalarVolTask


def test_affScalarVolTask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_target=dict(
            argstr='-target %s',
            position=2,
        ),
        in_volume=dict(
            argstr='-in %s',
            exists=True,
            mandatory=False,
            position=0,
        ),
        in_xfm=dict(
            argstr='-trans %s',
            exists=True,
            mandatory=False,
            position=1,
        ),
        out_file=dict(
            argstr='-out %s',
            mandatory=False,
            name_source='in_volume',
            name_template='%s_affxfmd.nii.gz',
            position=3,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = affScalarVolTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_affScalarVolTask_outputs():
    output_map = dict(out_file=dict(), )
    outputs = affScalarVolTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
