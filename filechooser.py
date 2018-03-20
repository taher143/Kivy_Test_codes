from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder

Builder.load_string('''

<FileChooserListView>:
    # --------------------
    # ADD BACKGROUND COLOR
    # --------------------
    canvas.before:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    layout: layout
    FileChooserListLayout:
        id: layout
        controller: root

[FileListEntry@FloatLayout+TreeViewNode]:
    locked: False
    entries: []
    path: ctx.path
    # FIXME: is_selected is actually a read_only treeview property. In this
    # case, however, we're doing this because treeview only has single-selection
    # hardcoded in it. The fix to this would be to update treeview to allow
    # multiple selection.
    is_selected: self.path in ctx.controller().selection

    orientation: 'horizontal'
    size_hint_y: None
    height: '48dp' if dp(1) > 1 else '24dp'
    # Don't allow expansion of the ../ node
    is_leaf: not ctx.isdir or ctx.name.endswith('..' + ctx.sep) or self.locked
    on_touch_down: self.collide_point(*args[1].pos) and ctx.controller().entry_touched(self, args[1])
    on_touch_up: self.collide_point(*args[1].pos) and ctx.controller().entry_released(self, args[1])
    BoxLayout:
        pos: root.pos
        size_hint_x: None
        width: root.width - dp(10)
        Label:
            # --------------
            # CHANGE FONT COLOR
            # --------------
            color: 0, 0, 0, 1
            id: filename
            text_size: self.width, None
            halign: 'left'
            shorten: True
            text: ctx.name
        Label:
            # --------------
            # CHANGE FONT COLOR
            # --------------
            color: 0, 0, 0, 1
            text_size: self.width, None
            size_hint_x: None
            halign: 'right'
            text: '{}'.format(ctx.get_nice_size())


<MyWidget>:
    FileChooserListView
''')

class MyWidget(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    TestApp().run()
