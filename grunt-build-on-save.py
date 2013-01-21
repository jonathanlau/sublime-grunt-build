import sublime, sublime_plugin,os

class BuildGruntOnSave(sublime_plugin.EventListener):

  def on_post_save(self, view):
    print 'BuildGruntOnSave: on_post_save'
    folder = view.window().folders()[0]
    os.chdir(folder)

    #let's see if project wants to be autobuilt.
    should_build = view.settings().get('build_on_save')
    if should_build == 1:
      #WINDOWS
      #view.window().run_command('exec',{'cmd':['grunt.cmd'],'working_dir':folder})
      
      #OSX
      view.window().run_command('exec',{'cmd':['grunt', '--no-color'],'working_dir':folder,'path':"/usr/local/bin"})
      #@path needs to point to the node + grunt binaries on your local file system.
      #These locations can vary depending on your chosen installation method. In most cases these binaries would be stored globally in "/usr/local/bin", however if you have choosen a different location or used an alternative method of installation i.e. NVM then these binaries will exist elsewhere. If the above fails, the commented "path" line should cover most bases HOWEVER you will need to populate the markers denoted by the [SQUARE BRACKETS] with your own information e.g. [USER] = your local username, [VERSION] = directory of the version of node you wish to adopt (if install via NVM).
      #view.window().run_command('exec',{'cmd':['grunt', '--no-color'],'working_dir':folder,'path':"/bin:/usr/bin:/usr/local/bin:/Users/[USER]/.nvm/bin:/Users/[USER]/.nvm/[VERSION]/bin"})
    else:
      print 'BuildGruntOnSave: Project not configured for build_on_save. Try setting "build_on_save=1" in project settings.sublime-project'