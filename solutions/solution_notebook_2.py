# let us perform a spectral measurement using all the data
datasets = Datasets(datasets=[*datasets_hess, *datasets_magic, datasets_lst[0]])
print(datasets)
# apply the model
datasets.model = [model]

# fit
results_joint = fit.run(datasets=datasets)
print(results_joint)
print(model.spectral_model)

# quickly compute spectral points for all the instruments
# - MAGIC
# -- assign the best fit model to the instrument data set
datasets_magic.models = [model]
# -- compute FPs
energy_edges_magic = datasets_magic[0].counts.geom.axes["energy"].edges
fpe_magic = FluxPointsEstimator(
    energy_edges=energy_edges_magic, source="CrabNebula", selection_optional="all"
)
flux_points_magic = fpe_magic.run(datasets=datasets_magic)
# - H.E.S.S.
# -- assign the best fit model to the instrument data set
datasets_hess.models = [model]
# -- compute FPs
energy_edges_hess = datasets_hess[0].counts.geom.axes["energy"].edges
fpe_hess = FluxPointsEstimator(
    energy_edges=energy_edges_hess, source="CrabNebula", selection_optional="all"
)
flux_points_hess = fpe_magic.run(datasets=datasets_hess)


# make the plot
fig, ax = plt.subplots()

# - references first
crab_meyer.plot(
    [e_min_lst, e_max_lst],
    ax=ax,
    label="Meyer et al. (2010)",
    color="k",
    ls="--",
    **plot_kwargs,
)
crab_magic.plot(
    [e_min_lst, e_max_lst],
    ax=ax,
    label="MAGIC Collaboration (2015)",
    color="dodgerblue",
    ls="--",
    **plot_kwargs,
)

# - joint result
spectral_model.plot(
    [e_min_lst, e_max_lst],
    ax=ax,
    color="gray",
    ls="-",
    label="joint likelihood fit",
    **plot_kwargs,
)
spectral_model.plot_error(
    [e_min_lst, e_max_lst], ax=ax, facecolor="gray", alpha=0.4, **plot_kwargs
)

# - flux points of the instruments
flux_points_lst.plot(ax=ax, sed_type="e2dnde", marker=".", color="darkorange", label="LST-1")
flux_points_magic.plot(ax=ax, sed_type="e2dnde", marker=".", color="crimson", label="MAGIC")
flux_points_hess.plot(ax=ax, sed_type="e2dnde", marker=".", color="teal", label="H.E.S.S.")

ax.set_xlabel(r"$E\,/\,{\rm GeV}$")
ax.set_ylabel(
    r"$E^2 {\rm d}\phi/{\rm d}E\,/\,({\rm TeV}\,{\rm cm}^{-2}\,{\rm s}^{-1})$"
)
ax.legend()
plt.show()
