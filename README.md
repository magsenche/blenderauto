
Blenderauto automates the generation and animation of 3D shapes using Blender scripting, creating customizable datasets for shape analysis and scalable for future enhancements like textures and complex interactions.

# Setup

Add blenderauto & python/site_packages of your virtual env into blender python_path for imports:

```bash
echo $BLENDERAUTO >> $BLENDER/$VERSION/python/lib/$PYTHONV/site-packages/blenderauto.pth
echo $VENV/lib/$PYTHONV/site-packages >> $BLENDER/$VERSION/python/lib/$PYTHONV/site-packages/venv_sp.pth
```
Where
- `$BLENDERAUTO` is your blender project directory
- `$BLENDER` is the directory where Blender is installed
- `$VERSION` is your Blender version (e.g. 3.2)
- `$PYTHONV` if your python version (e.g python3.10)
- `$VENV` is your venv directory

Adding these paths will allow blender bundled python to find correct installed packages, although their might be some errors with specific packages (e.g. sklearn)
